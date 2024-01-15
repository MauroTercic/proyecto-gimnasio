import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

cursor = connection.cursor()

class UserActions:

    def __init__(self, username):
        cursor.execute("SELECT usuario FROM usuarios WHERE usuario=:usuario", {'usuario':username})
        self.username = cursor.fetchone()[0]


    def view_user(self):
        lst = ["usuario", "clave", "nombre", "apellido", "peso", "masa", "grasa", "cintura",
            "brazo", "pierna", "pecho", "pecho_respirado", "brazo_trabado", "altura", "edad"]
        
        cursor.execute("SELECT * FROM usuarios WHERE usuario=:usuario", {'usuario': self.username})
        counter = 0
        for i in cursor.fetchone()[1:]:
            print(f"{lst[counter]}: {i}")
            counter += 1


    def delete_user(self):
        # La seleccion del usuario a actualizar se va a hacer automatica de acorde al usuario loggeado, este metodo es temporal. El resto queda igual
        cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario='{self.username}'")
        usuario = cursor.fetchone()[0]

        print(f"¿Quieres borrar este usuario? {usuario}")

        # Ese input va a ser cambiado por el input del front
        if input("Si/No: ").lower() == "si":
            if input("¿Esta realmente seguro, los cambios son irreversibles?\nSi/No: ").lower() == "si":
                cursor.execute(f"DELETE FROM usuarios WHERE usuario = '{usuario}'")
                print(f"Usuario {usuario} correctamente eliminado.")
            
        connection.commit()
        connection.close()   
        

