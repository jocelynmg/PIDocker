import usuarios.conexion as conexion

connect = conexion.connectarBD()
database = connect[0]
cursor = connect[1]


class Ejercicio:

    def __init__(self, usuario_id, tipo, descripcion):
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.descripcion = descripcion

    def guardarAvance(self):
        sql = "INSERT INTO notas VALUES(default, %s, %s)"
        avance = (self.usuario_id, self.tipo, self.descripcion)

        cursor.execute(sql, avance)
        database.commit()

        return [cursor.rowcount, self]