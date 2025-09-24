import mysql.connector 
import os

with open ('passwordBDD.txt', 'r') as archivo: #abro el archivo que tiene mi contraseña
    password = archivo.read()

def getConexion():#Conexion a la base de datos.
    conexion= mysql.connector.connect(
        user= 'root',
        password= password, #lo pongo asi para cuando lo publique en github no lo vea todo el mundo
        host= 'localhost',
        database= 'registro_usuarios',
        port= 3306)
    return conexion
