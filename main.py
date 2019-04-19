from flask import Flask
from flask import request
from pymongo import MongoClient
import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client.demo
collection = db.memee
app = Flask(__name__)

@app.route('/')
def hello_world():
    post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
    post_id = collection.insert_one(post).inserted_id
    return 'Hello World!'


@app.route('/data/', methods=['GET'])
def insert():
    print(request.json)
    if request.method == 'GET':
        result = request.json
        collection.insert(result)
    return "it worked!\n"

if __name__ == '__main__':
    app.run(debug=True)

