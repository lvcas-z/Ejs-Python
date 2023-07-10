database = {}

def registroUsuarios (db):
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese la contrasenia de usuario: ")
    db[username]=password

registroUsuarios(database)
registroUsuarios(database)
registroUsuarios(database)
registroUsuarios(database)

def leerDb (db):
    print("La informacion almacenada en la base de datos es : ")
    for key, value in db.items():
        print(f"{key} {value}")

leerDb(database)

def login(db):
    username = input("Ingrese su nombre de usuario: ")
    if (username in db):
        user_password = db.get(username)
        password = input("Ingrese la contrasenia de usuario: ")
        if(password == user_password):
            print("Iniciaste Sesion")
        else:
            print("Contrasenia incorrecta")
    else:
        print(f"No existe el usuario con nombre : {username}")

login(database)