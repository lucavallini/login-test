import mysql.connector 
import os

with open ('passwordBDD.txt', 'r') as archivo:
    password = archivo.read()

def getConexion():#Conexion a la base de datos.
    conexion= mysql.connector.connect(
        user= 'root',
        password= password,
        host= 'localhost',
        database= 'registro_usuarios',
        port= 3306)
    return conexion