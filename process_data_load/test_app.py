from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
from process import process_operate
from database import quality_data_list,machine_data_list
import datamake


@app.route('/chart')
def chart():
    return render_template('test_load_chart.html')

@app.route('/home')
def home():
   return render_template('home.html')

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
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        temp2_0 = request.args.get('char2_0')
        temp2 = request.args.get('char2')
        temp2_1 = request.args.get('char2_1')
        content_list = quality_data_list.get_quality_data_list(temp2_0, temp2, temp2_1)

    # now = datetime.today()
    # content_list.append(now)

        html = render_template('quality_load.html', quality_data_list=content_list, char2_0=temp2_0, char2=temp2, char2_1=temp2_1)
        return html


@app.route('/machine_load', methods=['POST', 'GET'])
def machine_data_load():
    if request.method == 'POST':
        #temp = request.form['num']
        pass
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
    return render_template('process_load',num=num)


@app.route('/dataopin',methods=['POST'])
def selectin(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('data_make',num=temp))



@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        temp1 = request.args.get('char1')
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('submit.html', char1=temp1)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)