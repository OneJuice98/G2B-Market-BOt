### G2B 나라장터 검색 봇

2021년 6월 13일 
Selenium을 활용해서 만들라 했는데, 생각보다 쉽지 않았다.. element를 못읽더라니깐? 네이버에서는 잘되는데,,, <br>
그래서 확장성은 상당히 낮지만,,, width, height = 1440, 900 이면 상당히 잘 이용할 것이라 생각한다. <br>
공사, 조경식재, 강원지역 선택 후 검색하는 기능까지 구현. <br>

2021년 6월 14일 
search.py 의 공사 검색 함수를 이용하여 Data.py에서 기간 상관없이 공사목록을 저장할 수 있게되었다. <br>
-> 추가해야 할 것. 날짜에서 '일'이 겹치는 현상이 있다. <br> 
현재 귀찮기도하고 어려울 것 같아서 아직 안만들었으니 만들도록 하자! <br>

참고 : http://hleecaster.com/narajangteo-crawling/ (파이썬으로 나라장터 입찰공고 크롤링하기) <br>

2021년 6월 15일 <br>
PyQt5 로 UI를 제작할려고 했다.. <br>
이제 DataFrame 형태로 입찰결과를 볼 수 있다. (BiddingList)<br>
workList 로 공사목록을 확인 할 수 있다. <br>



--> Django, MySQL 등 잘 골라서 DB를 겹치지 않게 저장하고 자동으로 업데이트되게 하고 싶다! <br>
--> 속도가 조금 느려서 데이터 크롤링 그 부분을 수정해야 할 것 같다.


