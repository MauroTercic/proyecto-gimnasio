import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

cursor = connection.cursor()

