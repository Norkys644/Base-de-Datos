import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # si no tienes contraseña
        database="tienda_db"
    )
