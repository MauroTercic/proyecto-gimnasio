from user import User



def create_user():
    # Crear lista con todos los atributos
    lst = ["usuario", "clave", "nombre", "apellido", "peso", "masa", "grasa", "cintura",
        "brazo", "pierna", "pecho", "pecho_respirado", "brazo_trabado", "altura", "edad"]
        
    # Diccionario vacio para poner los atributos y sus valores de acorde a los inputs del usuario
    dic = {}

    for i in lst:
        dic[i] = input(f"{i}: ")


    usuario = User(dic[lst[0]], dic[lst[1]], dic[lst[2]], dic[lst[3]], dic[lst[4]], dic[lst[5]], dic[lst[6]], dic[lst[7]], dic[lst[8]], dic[lst[9]],
                dic[lst[10]], dic[lst[11]], dic[lst[12]], dic[lst[13]], dic[lst[14]])
    
    usuario.commit_user()


create_user()