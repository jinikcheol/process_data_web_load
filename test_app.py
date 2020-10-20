from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
from process import process_operate
from database import data_list,machine_data_list
import datamake

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/')
def Korenas_monitoring():
    return render_template('Korens_monitoring.html')

@app.route('/load')
def data_load():

    content_list = data_list.get_datalist()

    # now = datetime.today()
    # content_list.append(now)

    html = render_template('data_lists.html', data_list=content_list)
    return html

@app.route('/machine_load')
def machine_data_load():

    content_list = machine_data_list.get_machine_data_list()

    # now = datetime.today()
    # content_list.append(now)

    html = render_template('machine_data_lists.html', machine_data_list=content_list)
    return html

@app.route('/data')
def data():
   return render_template('index.html')

@app.route('/dataop')
def dataop():
   return render_template('data_OP.html')

@app.route('/monitor')
def monitor():
   return process_operate.process_start(4)

@app.route('/<int:num>')
def inputData(num=None):
    return render_template('data_makes.html',num=num)


@app.route('/dataopin',methods=['POST'])
def selectin(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('data_make',num=temp))

@app.route('/makes')
def data_make():
    makes_list = datamake.get_datamakes()

    # now = datetime.today()
    # content_list.append(now)

    html = render_template('data_makes.html', data_list=makes_list)
    return html

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)