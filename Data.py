"""
    최근 몇개월 간 특정 지역의 공사 정보를 리스트에 저장함. (workList)
    입찰 결과까지 저장함. (BiddingList)
"""


from selenium import webdriver
from search import searchTask
import pandas as pd
from collections import deque


# 연도, 월, 일 입력 // '일' 은 반드시 같게 해주세요!
def parse_G2B(kind, start, end, add):
    
    #start = [2020, 6, 14]
    #end = [2021, 6, 14]
    check, count = False, 0
    workList = []
    while True:
        if count == 0:
            tempStart = start
            # add 개월 간격으로 검색.
            tempEnd = [start[0], start[1] + add, start[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            count += 1
        else:
            tempStart = [int(tempEnd[0]), int(tempEnd[1]), int(tempEnd[2])]
            print(tempEnd)
            tempEnd = [tempStart[0], tempStart[1] + add, tempStart[2]]
            if tempEnd[1] > 12:
                tempEnd[0] += 1
                tempEnd[1] -= 12
            if tempEnd[0] == end[0] and tempEnd[1] == end[1]:
                check = True
            elif tempEnd[0] == end[0] and tempEnd[1] > end[1]:
                tempEnd[1] = end[1]
                check = True
       
        workList.extend(searchTask('공사', '강원', kind, '강원도 횡성군', tempStart, tempEnd))

        if check: # 수정해야함.!
            break
        

    try:
        
        driver = webdriver.Chrome('/Users/waterpurifier/Downloads/chromedriver')
        BiddingList = []
        priceList = []
        for result in workList:
            driver.get(result[2])
            try:
                price =[]
                try:
                    basic = driver.find_element_by_class_name('tr')
                    basic = basic.text
                except Exception as e:
                    print(e)
                    basic = ''
                    pass
                price.append(result[1])
                price.append(basic)
                priceList.append(price)
                click = driver.find_element_by_xpath('//*[@id="container"]/div[24]/table/tbody/tr/td[5]/a/span')
                click.click()
                elem = driver.find_element_by_class_name('results')
                div_list = elem.find_elements_by_tag_name('div')
                biddingResult = []
                cnt = 0
                for div in div_list:
                    biddingResult.append(div.text)
                    if cnt == 8:
                        biddingResult.append(basic)
                        cnt = -1 
                    cnt += 1
                BiddingList.append([biddingResult[i * 10:(i + 1) * 10] for i in range((len(biddingResult) + 10 - 1)// 10)])
                
            except:
                pass
        ####
        df = pd.DataFrame(columns=['순위', '사업자 등록번호', '업체명', '대표자명', '입찰금액', '투찰률', '추첨 번호', '투찰일시', '비고', '기초금액'])
        count = 0
        price_df = pd.DataFrame(columns=['공고번호', '기초금액'])
        count_price = 0
        for idx in priceList:
            price_df.loc[count_price] = idx
            count_price += 1
        for idx in range(len(BiddingList)):
            for j in BiddingList[idx]:
                if len(j) == 10:
                    temp = deque(j)
                    #temp.appendleft(workList[idx][1])
                    df.loc[count] = list(temp)
                    count += 1

        # 업무, 공고번호-차수, 분류, 공고명, 공고기관, 수요기관, 계약방법, 입력일시(입찰마감일시), 바로가기
        work = pd.DataFrame(columns=['업무', '공고번호', '분류', '공고명', '공고기관', '수요기관', '계약방법', '입력일시', '투찰' ,'바로가기'])
        count = 0
        for w in workList:
            t = w[:2] + w[3:5] + w[6:10] + w[11:12]
            t.append(w[2])
            work.loc[count] = t
            count += 1

        return df, work, price_df
        #return workList, BiddingList
    except Exception as e:
        # 위 코드에서 에러가 발생한 경우 출력
        print(e)
    finally:
        # 에러와 관계없이 실행되고, 크롬 드라이버를 종료
        driver.quit()