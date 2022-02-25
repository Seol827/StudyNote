from flask import Flask, render_template, request, jsonify, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'seora'

import config

from pymongo import MongoClient

client = MongoClient(config.Mongo_key)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book')
def book():
    return render_template('search.book.html')

@app.route('/todo/home')
def todo_home():
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
            user_id = check_user_id.get("ID")
            session['userid'] = user_id
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
            print('fail');
    return 'success'


### to do list ###
@app.route("/todo", methods=["POST"])
def todo_post():
    all_todos = list(db.todos.find({}, {'_id': False}))
    count = len(all_todos) + 1
    todo_receive = request.form['todo_give']

    id = session['userid']

    doc = {
        'userid' : id,
        'num' : count,
        'todo' : todo_receive,
        'done' : 0
    }

    db.todos.insert_one(doc)

    return redirect("/todo/home")


@app.route("/todo/done", methods=["POST"])
def todo_done():

    num_receive = request.form['num_give']
    db.todos.update_one({'num' : int(num_receive)},{'$set' : {'done': 1} })
    return redirect("/todo/home")


@app.route("/todo", methods=["GET"])
def todo_get():
    id = session['userid']

    todo_list = list(db.todos.find({'userid':id}, {'_id': False}))

    return jsonify({'todos': todo_list})


@app.route("/todo", methods=["DELETE"])
def todo_delete():

    num_receive = request.form['num_give']
    db.todos.delete_one({'num': int(num_receive)})

    return 'success'


@app.route("/todo/undo", methods=["POST"])
def todo_undo():
    num_receive = request.form['num_give']
    db.todos.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})

    return redirect("/todo/home")

# @app.route("/todo/id", methods=["GET"])
# def todo_id():
#     id = list(db.user.find({}, {'_id': False, 'password': False, 'name' : False}))
#
#     return jsonify({'id': id})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)