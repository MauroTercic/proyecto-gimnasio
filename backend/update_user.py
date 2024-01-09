import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

#connection.row_factory = lambda cursor, row: row[0]

cursor = connection.cursor()

def update_user(user):
    
    # La seleccion del usuario a actualizar se va a hacer automatica de acorde al usuario loggeado, este metodo es temporal. El resto queda igual
    cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{user}'")
    print(cursor.fetchone()[1:])
    
    # Elegir que se quiere actualizar 



update_user("vivaperon")