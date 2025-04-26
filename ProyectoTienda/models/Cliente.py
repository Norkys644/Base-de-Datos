from database.conexion import conectar

class Cliente:
    def __init__(self, nombre, apellidos, email, historial_compras=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.historial_compras = historial_compras

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (nombre, apellidos, email, historial_compras) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.apellidos, self.email, self.historial_compras))
        conexion.commit()
        conexion.close()

    # Métodos para actualizar, eliminar, listar también se agregan aquí
