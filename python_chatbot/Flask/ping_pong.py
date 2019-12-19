from flask import Flask, render_template, request

# name을 app으로 실행한다. 
app = Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # name으로 저장된 값을 저장해서 pong 에게 넘겨준다 
    # ping에서 온 요청을 저장
    data = request.args.get('keyword')
    return render_template('pong.html', data = data)

@app.route('/naver')
def naver():
    # data = request.args.get('query')
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

if __name__=="__main__":
    app.run(debug=True)
    # 개발자모드로 하여 플라스크가 새로고침만 하면 반영되게끔 한다. 