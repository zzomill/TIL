from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg2')
def opgg2():
    data = request.args.get(name)
    return render_template('opgg2.html', userName = data)

# if __name__ == ("__main__"):
#     app.run(debug=True) 