from flask import Flask, render_template, redirect, request, url_for, jsonify,  make_response
from process import process_operate
from database import quality_data_list, machine_data_list
import datamake
import json
from time import time
import pymysql

#import datetime
#import flask_monitoringdashboard as dashboard
#from testing import testing_operate

app = Flask(__name__)

app.count = 0


@app.route('/data.json')
def date():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine ")
    results = cursor.fetchall()

    return json.dumps(results)


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/OEE')
def OEE():
    return render_template('OEE_index.html')


@app.route('/livechart_Electronic')
def livechart_Electronic():
    return render_template('Electronic_index.html')


@app.route('/livechart_Temperature')
def livechart_Temperature():
    return render_template('Temperature_index.html')

@app.route('/livechart_ProcessTime')
def livechart_ProcessTime():
    return render_template('ProcessTime_index.html')


@app.route('/live_resource')
def live_resource():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    cursor.execute("SELECT process_time from machine ")
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/live_Electronic')
def live_Electronic():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
    cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/live_Temperature')
def live_Temperature():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
    cursor.execute("SELECT machine_data from machine where machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/live_ProcessTime')
def live_ProcessTime():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    cursor.execute("SELECT process_time from machine ")
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/chart')
def chart():
    return render_template('test_load_chart.html')


@app.route('/home')
def home():
    return render_template('Home_index.html')
    #return render_template('home.html')


@app.route('/')
def Korenas_monitoring():
    return render_template('Korens_monitoring.html')


@app.route('/process_load', methods=['POST', 'GET'])
def process_data_load(num=None):
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        temp3 = request.args.get('char3')

        process_list = datamake.get_datamakes(temp3)

    # now = datetime.today()
    # content_list.append(now)

        html = render_template('process_load.html', process_data_list=process_list, char3=temp3)
        return html


@app.route('/quality_load', methods=['POST', 'GET'])
def quality_data_load():
    product = {}
    if request.method == 'POST':
        product['product_test'] = request.form.get('product_test')
        #return render_template('test_load_chart.html') #, test=temp_test)
        return jsonify(product)

    elif request.method == 'GET':
        temp2_0 = request.args.get('char2_0')
        temp2 = request.args.get('char2')
        temp2_1 = request.args.get('char2_1')
        content_list = quality_data_list.get_quality_data_list(temp2_0, temp2, temp2_1)

    # now = datetime.today()
    # content_list.append(now)

        html = render_template('quality_load.html', quality_data_list=content_list, char2_0=temp2_0, char2=temp2, char2_1=temp2_1)
        #html = render_template('Quality_index.html', quality_data_list=content_list, char2_0=temp2_0, char2=temp2, char2_1=temp2_1)
        return html


@app.route('/machine_load', methods=['POST', 'GET'])
def machine_data_load():
    if request.method == 'POST':
        return render_template('livechart.html')

    elif request.method == 'GET':
        temp1_0 = request.args.get('char1_0')
        temp1 = request.args.get('char1')
        temp1_1 = request.args.get('char1_1')
        content_list = machine_data_list.get_machine_data_list(temp1_0, temp1, temp1_1)

        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        html = render_template('machine_load.html', machine_data_list=content_list, char1_0=temp1_0, char1=temp1, char1_1=temp1_1)
        return html
    # now = datetime.today()
    # content_list.append(now)


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
    return render_template('process_load', num=num)


@app.route('/dataopin', methods=['POST'])
def selectin(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('data_make', num=temp))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)