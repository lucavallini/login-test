import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from stylesheet import RegisterStyle, LoginStyle
from conexion import getConexion
import mysql.connector
from db_operations import DatabaseManager

# Esto es toda la logica de botones, que hace cada uno, errores
# Falta tambien una biblioteca para que las contraseñas esten hasheadas.

class VentanaLogin(LoginStyle):
    def __init__(self):
        super().__init__()

        self.conexion = getConexion()# instanciamos
        self.db_manager = DatabaseManager(self.conexion) #instanciamos

        self._register_button.clicked.connect(self.open_register_window)#boton para iniciar registro
        self._login_button.clicked.connect(self.log_attemp)#boton loggin


    def log_attemp(self):#metodo para checkear si campos estan llenos
        user = self._user_input.text().strip()
        password = self._password_input.text().strip()
        if not user or not password:
            QMessageBox.critical(self,'Error','Rellene los campos user y password.')
            return
        
        self.loguear_user(user, password) #llamo para loguear con los parametros asignados

    
    def loguear_user(self, user, password):
        try:    
            resultado = self.db_manager.getLogin(user, password) #utilizo meotodo para logear y se le asigna a valores a resultado
            if resultado:
                user_id , user = resultado # resultado es una tuppla con dos valores, los dos valores son asignados a user_id y a user
                QMessageBox.information(self, 'Exito', f'Bienvenido {user}')
                self.close()
            else:
                QMessageBox.critical(self, 'ERROR', 'Usuario o contraseña incorrecta')

        except Exception as e:
            QMessageBox.critical(self, 'Error', 'Error en la conexion')



    #APRETAR REGISTER ABRA OTRA VENTANA
    def open_register_window(self):
        self.reg_window = VentanaRegister(self.db_manager)
        self.reg_window.show()



class VentanaRegister(RegisterStyle):
    def __init__(self, db_manager):
        super().__init__()

        self.db_manager = db_manager #instanciamos


        self._register_button.clicked.connect(self.register_attempt)#boton para registrar, va a checkear q campos esten completados

    def register_attempt(self): #intento para registrar, verifica campos llenos y registra
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

        # Si pasa las validaciones, crear usuario, pasamos valores 
        self.create_user(user, password)


    def create_user(self, user, password):
        try:
            if self.db_manager.getUser(user): # modulo getuser, que busca el nombre de usuario que este en el input, si esta es error, no se puede usar el mismo usuario
                QMessageBox.critical(self,'ERROR', 'Usuario ya existe')
                return

            self.db_manager.setRegister(user, password)# si pasa el if, crea usuario
            QMessageBox.information(self, 'Exito', f'¡Gracias por registrartre! Bienvenido a la comunidad {user}')
            self.close()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al registrar: {str(e)}')

