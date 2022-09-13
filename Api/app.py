from crypt import methods
from flask import Flask, jsonify, request, render_template

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
    return render_template('index.html')

@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_Store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_Store)
    return jsonify(new_Store)

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': ' Store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items '])
    return jsonify({'message': ' store not found'})


app.run(port = 5000)