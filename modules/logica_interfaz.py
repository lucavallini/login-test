import sys
from PyQt5.QtWidgets import QMessageBox, QTextEdit
from Assets.styles.stylesheet import registerStyle, loginStyle, mainWindowStyle
from database.conexion import getConexion
from database.db_operations import DatabaseManager
from api.nasa_api import nasaApi

# Esto es toda la logica de botones, que hace cada uno, errores
# Falta tambien una biblioteca para que las contraseñas esten hasheadas.

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
            QMessageBox.critical(self, 'Error', 'Error en la conexion')
        

    #APRETAR REGISTER ABRA OTRA VENTANA
    def open_register_window(self):
        self.reg_window = ventanaRegister(self.db_manager)
        self.reg_window.show()



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



class ventanaMain(mainWindowStyle): #ventana principal, despues de loguearse
    def __init__(self, db_manager, user): #hereda la instancia de db_manager
        super().__init__()

        self.db_manager = db_manager
        self.user = user
        self.api = nasaApi() #instancia de la api de nasa
        

        self._user_button.clicked.connect(self.show_user_info) #boton para ver info del user



    def setText(self, text):
        if not hasattr(self, "api_text"):
            self.api_text = QTextEdit()
            self.api_text.setReadOnly(True)
            self.content_layout.addWidget(self.api_text)
        self.api_text.setText(text)



    def show_user_info(self):
        resultado = self.db_manager.getUser(self.user) #uso el metodo para obtner el nombre de usuario, y lo devuelve en una tuppla
        
        if resultado:
            username = resultado[0] #la tupla q nos devuelve getuser, agarramos el primer valor(user)
            QMessageBox.information(self, 'Datos del usuario', f'Usuario: {username}')
    


    def setClear_area(self):#metodo para limpiar el area del contenido
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()