import requests # requests모듈 가져옴 
#html을 파이썬이 읽을 수 있게 가져온다 
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

# requests 모듈로 url내용을 get방식으로 텍스트로 가져온다 
req = requests.get(url).text

print(req)

# soup에서 req로 html을 읽을수 잇게 가져온다 
soup = BeautifulSoup(req, 'html.parser')
#print(soup) => 에러(인코딩 불가)

#셀렉터를 포함하고 있는 애들이 다 카피된다 (원하는 텍스트만 추출하기)
# exchange = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
# print(exchange.text)