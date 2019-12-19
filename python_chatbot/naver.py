import requests
from bs4 import BeautifulSoup

url = 'https://naver.com'
req = requests.get(url).text
data = BeautifulSoup(req, 'html.parser')


# numbers = list(range(1:20))

# for number in numbers:
sel = '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(6) > li > a > span.ah_k'
search = data.select(sel)

print(search)
for item in search : 
    print(item.text)