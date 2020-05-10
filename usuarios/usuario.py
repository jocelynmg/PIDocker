import hashlib
import usuarios.conexion as conexion

#Se crea una instancia de la conexión a la BD
connect = conexion.connectarBD()
database = connect[0]
cursor = connect[1]

class Usuario:
    """Define un usuario con nombre, username y contraseña"""

    #Constructor de Usuario
    def __init__(self, nombre, username, password):
        self.nombre = nombre
        self.username = username
        self.password = password

    #Método para la inserción del usuario a la BD
    def insercionBD(self):
        #Cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Query para la inserción del usuario a la BD
        sql = "INSERT INTO Usuarios VALUES(default, %s, %s, %s)"
        usuario = (self.nombre, self.username, cifrado.hexdigest())
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            resultado = (cursor.rowcount, self)

        #Cacha el error cuando el username ya existe
        except conexion.mysql.connector.IntegrityError as err:
            print('Error: {}'.format(err))
            resultado = [0, self]

        return resultado

    #Método para la lectura del usuario desde la BD
    def identificarseBD(self):

        #Query para validar usuario en la BD
        sql = "SELECT * FROM Usuarios WHERE username = %s AND passwd = %s"

        #Cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.username, cifrado.hexdigest())

        #Manda el query y regresa la tupla del usuario si coincide
        cursor.execute(sql, usuario)
        resultado = cursor.fetchone()

        return resultado