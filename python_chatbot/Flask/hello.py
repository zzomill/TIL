from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

#플라스크가 실행하는 주소에서 요청을 보내는 곳 (hello) dycjd 
@app.route('/')
def hello():
    name = request.args.get("name", "KK")
    return f'Hello, {escape(name)}!'
#문자열이 끝나버리는 경우 

# @app.route('/fstring')
# def fstring():
#     fstring = "조미래"
#     #변수를 문자열 안에서 부를 수 있다. 
#     return f"제 이름은 {fstring} 입니다.".


#부여된 주소 뒤에 /hi를 붙이면
# http://127.0.0.1:5000/  + route부분 추측 로컬호스트 

@app.route('/hi')
def hi():
    name = "조미래"
    # html에 념겨줄 변수 이름 = name 변수 
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>/')
def greeting(name) :
    def_name = name
    return render_template('greeting.html', html_name = name)

# 무조건 숫자로 넘어올 때만 진행한다. 
#@app.route을 통해서 () 를 실행한다. 

@app.route('/cube/<int:num>')
def cube(num) :
    # html에게 넘겨주는 변수 
    # def_num = num
    cube_num = num**3
    return render_template('cube.html', def_num = num, cube_num = cube_num)

@app.route('/dinner')
def dinner():
    # 랜덤으로 출력 리스트 만들기 
    menu = ['김밥', '라면', '스테이크', '훠거']
    dinner = random.choice(menu)

    menu_img = { '김밥' : 'http://recipe1.ezmember.co.kr/cache/recipe/2016/11/28/6bc7f3c7a3fdf517e6943dd14a9b3df01.jpg' ,
     '라면' : 'http://static.hubzum.zumst.com/hubzum/2019/04/19/13/694050ce163a4655bc5032ac11e0bcd5.jpg',
        '스테이크' : 'http://recipe1.ezmember.co.kr/cache/recipe/2017/01/06/43c256e93d9c18240a3c5ed7ee3f55051.jpg', 
        '훠거' : 'https://mblogthumb-phinf.pstatic.net/MjAxODA0MDNfNDQg/MDAxNTIyNzYwNzIyOTUy.tzjCX7fhpMq4jeVXaz5TwvjqL7nbOteLkC_Sy5U39tsg.W4vb2h6Ru-UqZhb0XpLMEDNtIruhuCWDdJ2V3yHlY7cg.JPEG.jn1224_/output_21740507.jpg?type=w800' }
    img_url = menu_img[dinner]
    # 하늘색 : html에게 넘겨줄 변수 
    return render_template('dinner.html', dinner = dinner, img_url = img_url)


@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', movies = movies)

if __name__=="__main__":
    app.run(debug=True)