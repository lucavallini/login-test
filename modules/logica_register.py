import sys
from PyQt5.QtWidgets import QMessageBox, QTextEdit
import requests
from Assets.styles.stylesheet import registerStyle, loginStyle, mainWindowStyle
from database.conexion import getConexion
from database.db_operations import DatabaseManager

class ventanaRegister(registerStyle):
    def __init__(self, db_manager): #hereda la la instancia de db_manager
        super().__init__()

        self.db_manager = db_manager #instanciamos


        self._register_button.clicked.connect(self.register_attempt)#boton para registrar, va a checkear q campos esten completados

    def register_attempt(self): #intento para registrar, verifica campos llenos y registra
        user = self._user_input_reg.text().strip()
        password = self._password_input_reg.text().strip()
        password_verify = self._password_input_reg_verify.text().strip()
        tamanio_clave = len(password)

        # Validaciones
        if not user or not password or not password_verify:
            QMessageBox.critical(self, 'Error', 'Rellene los campos y vuelva a intentar')
            return
        
        if tamanio_clave < 6:
            QMessageBox.critical(self, 'Error', 'La contraseña debe tener al menos 6 caracteres')
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
            QMessageBox.information(self, 'Exito', f'¡Gracias por registrarte! Bienvenido a la comunidad {user}!')
            self.close()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al registrar: {str(e)}')