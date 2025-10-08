#Aca irian todas las querys y operaciones q se hagan en la base de datos, para ser reutilizables y que no este todas en logica_interfaz
import mysql.connector
from database.conexion import getConexion

class DatabaseManager:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor() #cursor busca lleva y trae

    def createTable(self):  # metodo para crear tabla si es q no existe
        query = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
        ''' #query para pasar a mysql
        self.cursor.execute(query) #ejecuta la query
        self.conexion.commit() #enviar query

    def setRegister(self, user, password):  # metodo para REGISTRAR
        query = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)' #query para pasar a mysql
        self.cursor.execute(query, (user, password)) #ejecuta cla query, con los valores user y password
        self.conexion.commit() # enviar query

    def getLogin(self, user, password):  # metodo para LOGUEAR
        query = 'SELECT id, username FROM usuarios WHERE username = %s AND password = %s' #query para mysql
        self.cursor.execute(query, (user, password)) #ejecuta query con los parametros
        return self.cursor.fetchone() #busca lleva y trae la primera linea 
    
    def getUser(self, user):  # metodo para BUSCAR NOMBRE USUARIO
        query = 'SELECT username FROM usuarios WHERE username = %s' #query para mysql
        self.cursor.execute(query, (user,)) #ejecuta query con el parametro
        return self.cursor.fetchone() #busca lleva y trae la primera linea, funcionaria como un LIMIT 1