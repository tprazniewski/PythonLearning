import sqlite3
from venv import create

connection  = sqlite3.connect('data.db')
cursor = connection.cursor()
#  auto incr column INTEGER PRIMARY KEY || we can't use int it must be INTEGER in that case
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)

connection.commit()
connection.close()