from crypt import methods
from flask import Flask, jsonify 

stores = [
    {
    'name': 'Salts Store',
    'items': [
        {
        'name': 'My item',
        'price': 20.99
        }
    ]
    }
]

app = Flask(__name__)

@app.route('/')
def home():
    return "First Api"

@app.route('/store/<string>:name')
def get_store(name):
    pass


@app.route('/store', methods = ['POST'])
def create_store():
    pass 

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods= ['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port = 5000)