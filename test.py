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
else:
    print("Error al conectar con MySQL")

# CREAMOS EL CURSOR
cursor = conexion.cursor()

#EJECUTAR LA CONSULTA
cursor.execute("select Name, population FROM city LIMIT 10")

# ODTENER LOS RESULTADOS
resultados = cursor.fetchall()

#IMPRIMIR LOS RESULTADOS
for ciudad in resultados:
    print(ciudad)

#CERRAMOS EL CURSOR Y LA CONECCION
cursor.close()
conexion.close()
