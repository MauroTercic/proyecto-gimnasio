import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

cursor = connection.cursor()

def delete_user(user):
    
    # La seleccion del usuario a actualizar se va a hacer automatica de acorde al usuario loggeado, este metodo es temporal. El resto queda igual
    cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario='{user}'")

    usuario = cursor.fetchone()[0]
    print(f"¿Seguro que quieres borrar este usuario? {usuario}")

    if input("Si/No: ").lower() == "si":
        cursor.execute(f"DELETE FROM usuarios WHERE usuario = '{user}'")
        print(f"Usuario {user} correctamente eliminado.")
    
    connection.commit()
    connection.close()


