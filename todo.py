from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
import config
client = MongoClient(config.Mongo_key)
db = client.dbsparta

@app.route('/')
def home():

    return render_template('todolist.html')

@app.route("/todo", methods=["POST"])
def todo_post():
    all_todos = list(db.todo.find({}, {'_id': False}))
    count = len(all_todos) + 1
    todo_receive = request.form['todo_give']

    doc = {
        'num' : count,
        'todo' : todo_receive,
        'done' : 0
    }

    db.todo.insert_one(doc)
    return jsonify({'msg': '저장완료!'})


@app.route("/todo/done", methods=["POST"])
def todo_done():

    num_receive = request.form['num_give']
    db.todo.update_one({'num' : int(num_receive)},{'$set' : {'done': 1} })
    return jsonify({'msg': '완료!'})


@app.route("/todo", methods=["GET"])
def todo_get():
    todo_list = list(db.todo.find({}, {'_id': False}))

    return jsonify({'todos': todo_list})

@app.route("/todo", methods=["DELETE"])
def todo_delete():

    num_receive = request.form['num_give']
    db.todo.delete_one({'num': int(num_receive)})

    return jsonify({'msg':'삭제완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
