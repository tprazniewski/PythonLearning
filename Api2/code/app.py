from flask import Flask
from flask_restful import  Api
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'tom'


# api works with resources and every resource works with the class
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# If we import this file to another file this won't be triggered , python asign __main__ to a current file name read: __name__ only when we trigger the app from terminal for example using python3 app.py
if __name__ == '__main__':
    app.run(port=5000, debug = True)