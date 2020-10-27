from flask import Flask, jsonify ,request, render_template

app = Flask(__name__)
# jsonify 한글로 인코딩
app.config['JSON_AS_ASCII'] = False
app.users = {}
app.id_count = 1
app.id_num = 1
# users 정보
app.users = {}
@app.route('/signup',methods=['GET','POST'])
def test():

    if request.method == 'POST':
        app.users['num']=app.id_num
        app.users['ID'] = request.form.get("id")
        app.users['Password'] = request.form.get("password")
        app.users['Name'] = request.form.get("name")
        app.users['Email'] = request.form.get("email")
        app.id_num= app.id_num+1
        #POST body에 정보 딕셔너리로 가지고 오기
        return jsonify(app.users)
    #회원가입 메뉴
    return render_template('test.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)