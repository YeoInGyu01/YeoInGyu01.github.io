import os
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL 데이터베이스 연결 정보
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'mydb'

# MySQL 연결 객체 생성
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/', methods=['GET','POST'])
def login_view():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        # 로그인 처리 코드 추가
        userid = request.form.get('아이디')
        password = request.form.get('비밀번호')
        # 데이터베이스에서 사용자 정보 조회
        cursor = mysql.cursor()
        sql = "SELECT * FROM member WHERE member_id = %s AND member_password = %s"
        values = (userid, password)
        cursor.execute(sql, values)
        user = cursor.fetchone()

        if user:
            # 로그인 성공 시 처리 코드 추가
            return redirect('/index')
        else:
            return "로그인 실패"
    
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        # 회원가입 처리 코드 추가
        userid = request.form.get('id')
        password = request.form.get('pw')
        password_2 = request.form.get('pw_ch')
        username = request.form.get('name')
        userphone = request.form.get('tel')
        useremail = request.form.get('email')
        useradd = request.form.get('address')
        userposition = request.form.get('position')




        if not (userid and password and password_2 and username):
            return "입력되지 않은 정보가 있습니다"
        elif password != password_2:
            return "비밀번호가 일치하지 않습니다"
        else:
            # 데이터베이스에 사용자 정보 저장
            cursor = mysql.cursor()
            sql = "INSERT INTO member (member_id,member_name,member_password,member_phone,member_email,member_address,member_position) VALUES (%s, %s, %s,%s,%s,%s,%s)"
            values = (userid, username, password , userphone, useremail, useradd, userposition)
            cursor.execute(sql, values)
            mysql.commit()
            return redirect('/')  # 회원가입 성공 후 로그인 페이지로 리다이렉트
    
@app.route('/Employee', methods=['GET','POST'])
def Employee():
    if request.method == 'GET':
        return render_template("Employee.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
