from database.conexion import conectar

class Producto:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.precio, self.stock, self.categoria))
        conexion.commit()
        conexion.close()

    # Métodos para actualizar, eliminar, listar también se agregan aquí
