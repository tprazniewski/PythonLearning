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
    
    def put(self, name):
        data = Item.parser.parse_args()

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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from items"
        result = cursor.execute(query)

        items = []
        
        for row in result:
            items.append({'name': row[0], 'price': row[1]})


        connection.close()

        return {'items': items}
