import mysql.connector 
import os
def getConexion():
    conexion= mysql.connector.connect(
        user= 'root',
        password= '47328448Luca_',
        host= 'localhost',
        database= 'registro_usuarios',
        port= 3306)
    return conexion

