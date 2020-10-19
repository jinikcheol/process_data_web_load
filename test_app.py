from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
from process import process_operate
from database import data_list

@app.route('/mypage')
def mypage():
   return process_operate.process_start(3)
@app.route('/load')
def index():

    content_list = data_list.get_datalist()

    # now = datetime.today()
    # content_list.append(now)

    html = render_template('data_lists.html', data_list=content_list)
    return html

@app.route('/data')
def data():
   return render_template('index.html')


@app.route('/monitor')
def monitor():
   return process_operate.process_start(3)


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)