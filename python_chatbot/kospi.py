import requests #모듈 가져옴 
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise"

# request = requests.get(url)
request = requests.get(url).text
# get방식으로 가져온다

# print(request)

#파이썬이 읽을 수 있게 html형식을 parsing(컴파일)한다. 
soup = BeautifulSoup(request, 'html.parser')
# print(soup)

# html에서 가져오려는 값의 select로 복사 
kospi = soup.select_one("#KOSPI_now")
print(kospi)