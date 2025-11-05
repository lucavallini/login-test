import sys
from PyQt5.QtWidgets import QMessageBox
from Assets.styles.stylesheet import loginStyle
from database.conexion import getConexion
from database.db_operations import DatabaseManager
from modules.logica_main_window import ventanaMain
from modules.logica_register import ventanaRegister

class ventanaLogin(loginStyle):
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
                QMessageBox.information(self, 'Exito', f'¡Bienvenido de nuevo {user}!')
                self.close()
                self.main_window = ventanaMain(self.db_manager, user) #le paso los parametros a la ventana principal
                self.main_window.show()
            else:
                QMessageBox.critical(self, 'ERROR', 'Usuario o contraseña incorrecta')
            
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error en la conexion {str(e)}')
        

    #APRETAR REGISTER ABRA OTRA VENTANA
    def open_register_window(self):
        self.reg_window = ventanaRegister(self.db_manager)
        self.reg_window.show()
