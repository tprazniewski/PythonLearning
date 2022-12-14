from flask import Flask, request
from flask_restful import Resource, reqparse
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help = "This field canot be left blank"
    )

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': "item not found"}, 404


        # next give us the first match, it ll break the program if tehre are no match. This is why we use None
        # item = next(filter(lambda item: item['name'] == name, items), None) # if it finds the match it ll return it
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item': None}, 404
        # return {'item': item}, 200 if item is not None else 404
        # return {'item': item}, 200 if item else 404

    @classmethod # cls because its a class method
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name =?"
        result = cursor.execute(query, (name,)) #the name is a tupple so reemmebr to have a coma if its a single value tupple
        row = result.fetchone()

        connection.commit
        connection.close

        if row:
            return {'item': row[0], 'price': row[1]}

    def post(self, name):
        # if Item.find_by_name(name):  its the same as the line below
        if self.find_by_name(name):
            return{'message': "An item with name '{}' already exists".format(name)}, 400 # sth went wrong with the request
        
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        
        try:
            self.insert(item)
        except:
            return{'message': " An error occured inserting the item"}, 500 #internal server error

        return item, 201


        # parser = reqparse.RequestParser()
        # parser.add_argument('price',
        #     type = float,
        #     required = True,
        #     help = ' This field cannot be blank '
        # )
        #is not none can be ommited because it is a default
        # if next(filter(lambda item: item['name'] == name, items), None) is not None:
        #     return {'message': "an item with the name: {} already exists".format(name)}, 400 # 400 is a bad request becaue it supposed to be solved on the clinets side
        # If the request doesn't attach the json payload or the request doesnt have the proper Content-type header request.get_json() ll give an error
        # force=True means we don't need content type header
        #data ll be a dictionary 
        # data = request.get_json(force=True)
        # item = {'name':name, 'price': data['price']}
        # items.append(item)
        # return item, 201
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        querry = "INSERT INTO items VALUES(?, ?)"

        cursor.execute(querry,(item['name'], item['price']))

        connection.commit()
        connection.close()


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))#the name is a tupple so reemmebr to have a coma if its a single value tupple

        connection.commit()
        connection.close()

        return { 'message': " Item deleted"}
        # global items
        # items = list(filter(lambda item: item['name'] !=name, items))
        # return {'message': 'item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']} #dictionary representing of each item

        if item is None:
            try: 
                self.insert(updated_item)
            except:
                return {'message': 'An error occured inserting the item'}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': 'An error occured updating the item'}, 500
                
        return updated_item

        # parser = reqparse.RequestParser()
        # parser.add_argument('price',
        #     type = float,
        #     required = True,
        #     help = "this field cannot be left blank"
        # )
        # # data = request.get_json()
        # data = parser.parse_args()

        # item = next(filter(lambda x: x['name'] == name, items), None)
        # print(item)
        # if item is None:
        #     item = {'name': name, 'price': data['price'] }
        #     items.append(item)
        # else:
        #     item.update(data)
        # return item
    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? where name=?"
        cursor.execute(query, (item['price'], item['name']))
        
        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):
        return{'items': items}
