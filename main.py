from flask import Flask, render_template, request, jsonify, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'seora'

import certifi

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zkful.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=certifi.where())
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/dbtest", methods=["GET"])
def homework_get():
    dblist = list(db.bucket.find({},{'_id':False}))
    print(dblist);
    return jsonify({'fans':dblist})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)