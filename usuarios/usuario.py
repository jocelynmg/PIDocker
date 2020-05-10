import hashlib
import usuarios.conexion as conexion

connect = conexion.connectarBD()
database = connect[0]
cursor = connect[1]

class Usuario:

    #Constructor de Usuario
    def __init__(self, nombre, username, password):
        self.nombre = nombre
        self.username = username
        self.password = password

    #Método para la inserción del usuario a la Base de Datos
    def insercionBD(self):
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO USUARIOS VALUES(null, %s, %s, %s)"
        usuario = (self.nombre, self.username, cifrado.hexdigest())
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            resultado = (cursor.rowcount, self)

        except conexion.mysql.connector.IntegrityError as err:
            print('Error: {}'.format(err))
            resultado = [0, self]

        return resultado

    #Método para la lectura del usuario de la Base de Datos
    def identificarseBD(self):

        #Consulta para validar usuario
        sql = "SELECT * FROM USUARIOS WHERE username = %s AND passwd = %s"

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.username, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result