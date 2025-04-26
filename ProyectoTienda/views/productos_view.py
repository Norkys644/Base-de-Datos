import tkinter as tk
from models.producto import Producto

class ProductosView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        # Entradas
        self.nombre = tk.Entry(root)
        self.nombre.pack()

        self.precio = tk.Entry(root)
        self.precio.pack()

        self.stock = tk.Entry(root)
        self.stock.pack()

        self.categoria = tk.Entry(root)
        self.categoria.pack()

        # Botones
        tk.Button(root, text="Agregar Producto", command=self.agregar_producto).pack()
        tk.Button(root, text="Informe Inventario Total", command=self.informe_inventario_total).pack()
        # Agregar más botones según los informes que piden

    def agregar_producto(self):
        nombre = self.nombre.get()
        precio = float(self.precio.get())
        stock = int(self.stock.get())
        categoria = self.categoria.get()
        
        producto = Producto(nombre, precio, stock, categoria)
        producto.guardar()
        print("Producto guardado exitosamente.")

    def informe_inventario_total(self):
        from database.conexion import conectar
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT SUM(precio * stock) FROM productos")
        resultado = cursor.fetchone()
        conexion.close()
        print(f"Valor total del inventario: {resultado[0]}")
