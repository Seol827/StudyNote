from json import dumps

import config
from flask import Flask, render_template, request, jsonify, redirect, session, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'seora'

client = MongoClient(config.Mongo_key)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book')
def book():
    return render_template('search.book.html')

@app.route('/todo')
def todo_show():
    return render_template('todolist.html')


@app.route('/loginresult', methods=["POST"])
def login_result():
    id_receive = request.form['userid']
    password_receive = request.form['psw']

    check_user_id = db.user.find_one({'ID': id_receive})

    if check_user_id is None:
        flash('회원 정보를 확인해 주세요.')
        return redirect('/')
    else:
        if check_user_id.get("password") == password_receive:
            user_name = check_user_id.get("name")
            session['userid'] = user_name
            return redirect("/")
        else:
            flash('회원 정보를 확인해 주세요.')
            return redirect("/")


@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect('/')


@app.route("/signup")
def signup_form():
    return render_template('signup.html')


@app.route("/signupresult", methods=["POST"])
def signup_result():
    id_receive = request.form['userid']
    password_receive = request.form['psw']
    irum_receive = request.form['irum']

    doc = {
        'ID': id_receive,
        'password': password_receive,
        'name': irum_receive
    }

    db.user.insert_one(doc)
    return redirect("/")


@app.route("/idcheck", methods=["POST"])
def id_check():
    id_receive = request.form['ID']

    check_user_id = db.user.find_one({'ID': id_receive})

    if check_user_id is not None:
        if check_user_id['ID']:
            return 'fail'
    return 'success'





if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
