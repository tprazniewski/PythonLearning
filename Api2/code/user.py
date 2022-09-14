import sqlite3
from flask_restful import Resource, reqparse

class User:
    
    def __init__(self, _id, user, password):
        self.id = _id
        self.user = user
        self.password = password
    
    # def find_by_username(self, username):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor() # is required to run a commands

    #     query = "SELECT * from users WHERE username=?"
    #     result = cursor.execution(query, (username),) # the parameters need to be in a forme of tupples in this case one argument this si the reason wh ywe have a comma
    #     row = result.fetchone()
    #     if row:
    #         user = User(row[0], row[1], row[2])
    #     else:
    #         user = None
    #     connection.close()
    #     return user
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() # is required to run a commands

        query = "SELECT * from users WHERE username=?"
        result = cursor.execution(query, (username),) # the parameters need to be in a forme of tupples in this case one argument this si the reason wh ywe have a comma
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() # is required to run a commands

        query = "SELECT * from users WHERE id=?"
        result = cursor.execution(query, (_id),) # the parameters need to be in a forme of tupples in this case one argument this si the reason wh ywe have a comma
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This felnd can not be blank"
    )

    parser.add_argument('password',
        type = str,
        required = True,
        help = "This felnd can not be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # Username and password need to be in tupple
        cursor.execute(query,(data['username'], data['password'],))

        connection.commit()
        connection.close()

        return{"message": "user created!"}