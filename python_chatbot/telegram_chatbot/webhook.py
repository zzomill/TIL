from decouple import config
import requests

#api 붙일 url

token = config('TELEGRAM_VOT_TOKEN')
url = "https://api.telegram.org/bot"

# ngrok 주고는 명령 창 다시 켤 때마다 바뀐다. 
paw_url =  'https://mirae9429.pythonanywhere.com'

#setWebhook을 하기 위한 요청은 get방식
data = requests.get(f'{url}{token}/setwebhook?url={paw_url}/{token}')
print(data.text)