import mysql.connector 
import os

with open ('passwordBDD.txt', 'r') as archivo: #abro el archivo que tiene mi contraseña
    password = archivo.read()

def createTable(self):  # metodo para crear tabla si es q no existe
    try:
        conexion = getConexion()
        cursor = conexion.cursor()
        query = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
        '''
        cursor.execute(query)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def getConexion():#Conexion a la base de datos.
    conexion= mysql.connector.connect(
        user= 'root',
        password= password, #lo pongo asi para cuando lo publique en github no lo vea todo el mundo
        host= 'localhost',
        database= 'registro_usuarios',
        port= 3306)
    return conexion

