#Aca irian todas las querys y operaciones q se hagan en la base de datos, para ser reutilizables y que no este todas en logica_interfaz

import mysql.connector
from conexion import getConexion

import mysql.connector
from conexion import getConexion

class DatabaseManager:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def setRegister(self, user, password):  # REGISTRAR

        query = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)'
        self.cursor.execute(query, (user, password))
        self.conexion.commit()

    def getLogin(self, user, password):  # LOGUEAR
        query = 'SELECT id, username FROM usuarios WHERE username = %s AND password = %s'
        self.cursor.execute(query, (user, password))
        return self.cursor.fetchone()
    
    def getUser(self, user):  # BUSCAR NOMBRE USUARIO
        query = 'SELECT username FROM usuarios WHERE username = %s'
        self.cursor.execute(query, (user,))
        return self.cursor.fetchone()