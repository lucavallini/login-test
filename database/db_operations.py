#Aca irian todas las querys y operaciones q se hagan en la base de datos, para ser reutilizables y que no este todas en logica_interfaz
import mysql.connector
from database.conexion import getConexion

class DatabaseManager:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor() #cursor busca lleva y trae

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
    

    def setNote(self, user_id, titulo, nota):
        query = 'INSERT INTO notas (titulo, nota, id) VALUES (%s, %s, %s)'
        self.cursor.execute(query, (titulo, nota, user_id))
        self.conexion.commit()


    def getTitles(self, user):
        query = 'SELECT titulo FROM notas WHERE id = %s' #query para mysql
        self.cursor.execute(query, (user,)) #ejecuta query con el parametro
        return self.cursor.fetchall() #busca lleva y trae todas las lineas

    def getNoteContent(self, user, titulo):
        query = 'SELECT nota FROM notas WHERE id = %s AND titulo = %s' #query para mysql
        self.cursor.execute(query, (user, titulo)) #ejecuta query con el parametro
        return self.cursor.fetchone() #busca lleva y trae la primera linea
    
    def deleteNote(self, user, titulo):
        query = 'DELETE FROM notas WHERE id = %s AND titulo = %s' #query para mysql
        self.cursor.execute(query, (user, titulo)) #ejecuta query con el parametro
        self.conexion.commit() # enviar query

    def getId(self, user):
        query = 'SELECT id FROM usuarios WHERE username = %s' #query para mysql
        self.cursor.execute(query, (user,)) #ejecuta query con el parametro
        return self.cursor.fetchone() #busca lleva y trae la primera linea