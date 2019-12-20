from flask import Flask, render_template, request
#(모듈명) (flask 안의 메소드)
from decouple import config
import requests
import random
app = Flask(__name__)

token = config('TELEGRAM_VOT_TOKEN')
chat_id = config('CHAT_ID')

url = 'https://api.telegram.org/bot'

@app.route('/')
def hello():
    return "Hello Mirae"

# 메세지를 작성할 곳 
@app.route('/write')
def write():
    return render_template('write.html')

# 메세지 보낼 곳 
@app.route('/send')
def send():
    # write.html에서 받아온 name = text 정보를 가져온다 
    text = request.args.get("text")
    #주소로 요청을으로 바로 실행한다. requests이용 (sendMessage 메소드를 사용) // getupdates(제이슨방식으로 가져옴 확인 가능)
    #챗봇이 메세지를 보낸다 
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

# 서버에서 접근할 수 있는 주소 
# 
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # print(request.get_json())// 텔레그램이 알려준 것 
    data = request.get_json()

    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    if text == "안녕":
        return_text = "hi."
    elif text == "로또":
        numbers = range(1, 46)
        return_text = sorted(random.sample(numbers,6))
    else :
        return_text = "지금 지원하는 텍스트는 안녕"
        
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}')
    return "ok", 200
    #다른 외부 id가 요청했을 때 그 사람에게 보내기  
    #updates 메소드 : 다른 사람의 정보가 쌓이게 되는 메소드 이용
    # chat_id = request.get_json.[][][]

if __name__=="__main__":
	app.run(debug=True)