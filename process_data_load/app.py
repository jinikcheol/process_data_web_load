from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
from process import process_operate

@app.route('/mypage')
def mypage():
   return process_operate.process_start(10)


@app.route('/data')
def data():
   return render_template('index.html')


@app.route('/monitor')
def monitor():
   return process_operate.process_start(3)


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)