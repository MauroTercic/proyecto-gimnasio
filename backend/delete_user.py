import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

cursor = connection.cursor()

def delete_user(user):
    
    # La seleccion del usuario a actualizar se va a hacer automatica de acorde al usuario loggeado, este metodo es temporal. El resto queda igual
    cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario='{user}'")

    usuario = cursor.fetchone()[0]
    print(f"¿Quieres borrar este usuario? {usuario}")

    # Ese input va a ser cambiado por el input del front
    if input("Si/No: ").lower() == "si":
        if input("¿Esta realmente seguro, los cambios son irreversibles?\nSi/No: ").lower() == "si":
            cursor.execute(f"DELETE FROM usuarios WHERE usuario = '{user}'")
            print(f"Usuario {user} correctamente eliminado.")
        
    connection.commit()
    connection.close()


delete_user("3")