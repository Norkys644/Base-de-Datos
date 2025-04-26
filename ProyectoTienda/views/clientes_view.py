import tkinter as tk
from models.cliente import Cliente
from database.conexion import conectar

class ClientesView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")

        # Entradas
        self.nombre = tk.Entry(root)
        self.nombre.pack()
        self.nombre.insert(0, "Nombre")

        self.apellidos = tk.Entry(root)
        self.apellidos.pack()
        self.apellidos.insert(0, "Apellidos")

        self.email = tk.Entry(root)
        self.email.pack()
        self.email.insert(0, "Email")

        # Botones
        tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente).pack(pady=5)
        tk.Button(root, text="Informe Compras por Cliente", command=self.informe_compras_cliente).pack(pady=5)
        tk.Button(root, text="Valor Total de Compras", command=self.valor_total_compras).pack(pady=5)

    def agregar_cliente(self):
        nombre = self.nombre.get()
        apellidos = self.apellidos.get()
        email = self.email.get()
        
        cliente = Cliente(nombre, apellidos, email)
        cliente.guardar()
        print("Cliente guardado exitosamente.")

    def informe_compras_cliente(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellidos, historial_compras FROM clientes")
        clientes = cursor.fetchall()
        conexion.close()

        print("\nHistorial de Compras por Cliente:")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Compras: ${cliente[3]}")

    def valor_total_compras(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT SUM(historial_compras) FROM clientes")
        resultado = cursor.fetchone()
        conexion.close()

        print(f"\nValor total de todas las compras: ${resultado[0]}")
