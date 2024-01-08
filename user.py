import sqlite3

FILE = "gimnasio.db"

connection = sqlite3.connect(FILE)

cursor = connection.cursor()


# Clase del usuario

class User:

    # Para evitar el error de un apty string que no se puede convertir en un float estan los if inline
    def __init__(self, usuario, clave, nombre, apellido, peso, masa, grasa, cintura,
                  brazo, pierna, pecho, pecho_respirado, brazo_trabado, altura, edad):
        self.usuario = usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.peso = float(peso) if peso != "" else 0
        self.masa = float(masa) if masa != "" else 0
        self.grasa = float(grasa) if grasa != "" else 0
        self.cintura = float(cintura) if cintura != "" else 0
        self.brazo = float(brazo) if brazo != "" else 0
        self.pierna = float(pierna) if pierna != "" else 0
        self.pecho = float(pecho) if pecho != "" else 0
        self.pecho_respirado = float(pecho_respirado) if pecho_respirado != "" else 0
        self.brazo_trabado = float(brazo_trabado) if brazo_trabado != "" else 0
        self.altura = float(altura) if altura != "" else 0
        self.edad = int(edad) if edad != "" else 0

    # Método que toma al usuario y lo introduce en la base de datos
    def commit_user(self):
        cursor.execute(f"""INSERT INTO usuarios (usuario, clave, nombre, apellido, peso, masa, grasa, 
                       cintura, brazo, pierna, pecho, pecho_respirado, brazo_trabado, altura, edad)
                       VALUES ("{self.usuario}", "{self.clave}", "{self.nombre}", "{self.apellido}", {self.peso}, {self.masa},
                       {self.grasa}, {self.cintura}, {self.brazo}, {self.pierna}, {self.pecho}, {self.pecho_respirado}, {self.brazo_trabado},
                       {self.altura}, {self.edad});""")
        
        # Para guardar los cambios en la base de datos
        connection.commit()
        connection.close()



"""
Ejemplos de creacion de usuarios manual

usuario_1 = User("vivaperon", "123", "mauro", "tercic", 80, 100, 150, 40, 20, 30, 60, 70, 40, 175, 22)
usuario_2 = User("jules", "asd", "julieta", "marino", 80, 100, 150, 40, 20, 30, 60, 70, 40, 175, 22)

usuario_1.commit_user()
usuario_2.commit_user()

"""

# Funcion descartable para crear la tabla

def create_table():
    cursor.execute("""CREATE TABLE usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                clave TEXT NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                peso REAL,
                masa REAL,
                grasa REAL,
                cintura REAL,
                brazo REAL,
                pierna REAL,
                pecho REAL,
                pecho_respirado REAL,
                brazo_trabado REAL,
                altura REAL,
                edad INTEGER
                )""")
    
    connection.commit()
    connection.close()    




