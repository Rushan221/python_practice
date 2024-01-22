from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/success/<int:score>")
def success(score):
    return render_template('result.html', marks=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', marks=score)

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        total_score = (science+math)/2
    result = ""
    if total_score >= 32:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result, score= total_score))

if __name__ == '__main__':
    app.run(debug = True)