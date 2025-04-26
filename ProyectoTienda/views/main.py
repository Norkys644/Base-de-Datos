import tkinter as tk
from views.productos_view import ProductosView
from views.clientes_view import ClientesView

def abrir_productos():
    ventana_menu.destroy()
    root = tk.Tk()
    ProductosView(root)
    root.mainloop()

def abrir_clientes():
    ventana_menu.destroy()
    root = tk.Tk()
    ClientesView(root)
    root.mainloop()

# Ventana principal (menú inicial)
ventana_menu = tk.Tk()
ventana_menu.title("Sistema de Gestión - Tienda")
ventana_menu.geometry("350x250")
ventana_menu.config(bg="#f0f0f0")  # Color de fondo suave

# Título
titulo = tk.Label(ventana_menu, text="Menú Principal", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=20)

# Botón Productos
btn_productos = tk.Button(
    ventana_menu, text="Gestión de Productos", font=("Arial", 14),
    width=25, height=2, bg="#4CAF50", fg="white", command=abrir_productos
)
btn_productos.pack(pady=10)

# Botón Clientes
btn_clientes = tk.Button(
    ventana_menu, text="Gestión de Clientes", font=("Arial", 14),
    width=25, height=2, bg="#2196F3", fg="white", command=abrir_clientes
)
btn_clientes.pack(pady=10)

ventana_menu.mainloop()
