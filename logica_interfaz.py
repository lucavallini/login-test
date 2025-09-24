import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from stylesheet import RegisterStyle, LoginStyle
from conexion import getConexion
import pymysql

# Esto es toda la logica de botones, que hace cada uno, errores
# Si bien las hay codigo de la conexion de la base de datos, luego debo transferirlas a otro archivo donde esten todos los querys para reutilizar y optmizacion de codigo(modulacion)
# Falta tambien una biblioteca para que las contraseñas esten hasheadas.

class VentanaLogin(LoginStyle):
    def __init__(self):
        super().__init__()

        self._register_button.clicked.connect(self.open_register_window)#boton para iniciar registro
        self._login_button.clicked.connect(self.log_attemp)#boton loggin


    def log_attemp(self):#metodo para checkear si campos estan llenos
        user = self._user_input.text().strip()
        password = self._password_input.text().strip()
        if not user or not password:
            QMessageBox.critical(self,'Error','Rellene los campos user y password.')
        
        self.loguear_user(user, password)

    
    def loguear_user(self, user, password):
        try:
            conexion = getConexion()
            cursor = conexion.cursor()
            login_query = "SELECT id, username FROM usuarios WHERE username = %s AND password = %s"
            cursor.execute(login_query, (user, password))
            resultado = cursor.fetchone()
            if resultado:
                user_id ,username = resultado
                QMessageBox.information(self, 'Éxito', f'Bienvenido {username}!')
                #ACA SE ABRIRIA UNA VENTANA PRINCIPAL 
                self.close()
                return True
            else:
                QMessageBox.critical(self, 'Error', 'Usuario o contraseña incorrecta')
                return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    #APRETAR REGISTER ABRA OTRA VENTANA
    def open_register_window(self):
        self.reg_window = VentanaRegister()
        self.reg_window.show()



class VentanaRegister(RegisterStyle):
    def __init__(self):
        super().__init__()

        self._register_button.clicked.connect(self.register_attempt)#boton para registrar, va a checkear q campos esten completados

    def register_attempt(self):
        user = self._user_input_reg.text().strip()
        password = self._password_input_reg.text().strip()
        password_verify = self._password_input_reg_verify.text().strip()

        # Validaciones
        if not user or not password or not password_verify:
            QMessageBox.critical(self, 'Error', 'Rellene los campos y vuelva a intentar')
            return

        if password != password_verify:
            QMessageBox.critical(self, 'Error', 'Las contraseñas no son iguales')
            return

        # Si pasa las validaciones, crear usuario
        self.create_user(user, password)


    def create_user(self, user, password):
        conexion = None
        cursor = None
        
        try:
            conexion = getConexion()
            cursor = conexion.cursor()
            
            # Verificar usuario existente
            check_query = "SELECT username FROM usuarios WHERE username = %s"
            cursor.execute(check_query, (user,))
            resultado = cursor.fetchone()
            if resultado:
                QMessageBox.warning(self, 'Error', 'El usuario ya existe')
                return
                
            # Insertar nuevo usuario
            query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
            cursor.execute(query, (user, password))
            conexion.commit()
            
            QMessageBox.information(self, 'Éxito', 'Usuario registrado exitosamente')
            self.close()
            

            
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

if __name__ == '__main__':
    print("Iniciando app...")  # debug
    app = QApplication(sys.argv)
    ventana_log = VentanaLogin()
    ventana_log.show()
    sys.exit(app.exec_())