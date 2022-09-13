import sqlite3
from venv import create

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # responsible for executing querries

create_table = "CREATE TABLE users(id int , user text, password text)" # schema

cursor.execute(create_table)

user = (1, 'tom','abcd')
insert_querry = "INSERT INTO users VALUES(?, ?, ?)"
# cursor.execute(insert_querry, user)

users = [
    (1, 'tom','abcd'),
    (2, 'trob','password')

]

cursor.executemany(insert_querry, users)


select_querry = "SELECT * FROM users"
for row in cursor.execute(select_querry):
    print(row)

connection.commit()
connection.close()