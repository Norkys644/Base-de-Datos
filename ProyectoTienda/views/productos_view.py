import tkinter as tk
from models.producto import Producto

class ProductosView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        # Configuración de colores
        self.bg_color = "#f4f4f4"
        self.entry_bg_color = "#e2e2e2"
        self.button_bg_color = "#4CAF50"
        self.button_fg_color = "#ffffff"

        # Entradas
        self.nombre = tk.Entry(root, bg=self.entry_bg_color)
        self.nombre.pack(pady=5)

        self.precio = tk.Entry(root, bg=self.entry_bg_color)
        self.precio.pack(pady=5)

        self.stock = tk.Entry(root, bg=self.entry_bg_color)
        self.stock.pack(pady=5)

        self.categoria = tk.Entry(root, bg=self.entry_bg_color)
        self.categoria.pack(pady=5)

        # Botones
        tk.Button(root, text="Agregar Producto", command=self.agregar_producto, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=5)
        tk.Button(root, text="Informe Inventario Total", command=self.informe_inventario_total, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=5)
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

