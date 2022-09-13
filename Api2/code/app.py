from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.secret_key = 'tom'


# api works with resources and every resource works with the class
api = Api(app)

items =[]

class Item(Resource):
    def get(self, name):
        # next give us the first match, it ll break the program if tehre are no match. This is why we use None
        item = next(filter(lambda item: item['name'] == name, items), None) # if it finds the match it ll return it
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item': None}, 404
        # return {'item': item}, 200 if item is not None else 404
        return {'item': item}, 200 if item else 404
    

    def post(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type = float,
            required = True,
            help = ' This field cannot be blank '
        )
        #is not none can be ommited because it is a default
        if next(filter(lambda item: item['name'] == name, items), None) is not None:
            return {'message': "an item with the name: {} already exists".format(name)}, 400 # 400 is a bad request becaue it supposed to be solved on the clinets side
        # If the request doesn't attach the json payload or the request doesnt have the proper Content-type header request.get_json() ll give an error
        # force=True means we don't need content type header
        #data ll be a dictionary 
        data = request.get_json(force=True)
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda item: item['name'] !=name, items))
        return {'message': 'item deleted'}
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type = float,
            required = True,
            help = "this field cannot be left blank"
        )
        # data = request.get_json()
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        print(item)
        if item is None:
            item = {'name': name, 'price': data['price'] }
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug = True)