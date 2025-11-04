import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sagitario14*",
    database="world"
)

if conexion.is_connected():
    print("conexion exitosa a MySQL")
    conexion.close()
else:
    print("Error al conectar con MySQL")
