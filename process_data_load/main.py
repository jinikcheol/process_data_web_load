from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
from process import process_operate

@app.route('/mypage')
def mypage():
   return '여기는 페이지에요!'


@app.route('/data')
def data():
   return render_template('index.html')


@app.route('/monitor')
def monitor():
   return process_operate.process_start(10)

@app.route('/')
@app.route('/<int:num>')
def inputData(num=None):
    return render_template('index.html',num=num)


@app.route('/selectin',methods=['POST'])
def selectin(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputData',num=temp))

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)