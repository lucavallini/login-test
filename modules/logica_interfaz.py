import sys
from PyQt5.QtWidgets import QMessageBox, QTextEdit
import requests
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
        
        self.test()

        self._user_button.clicked.connect(self.show_user_info) #boton para ver info del user


        #acciones de los botones del menu
        self.apod_content_action.triggered.connect(self.load_apod_content) #accion para ver contenido apod
        self.apod_about_action.triggered.connect(self.show_apod_info) #accion para ver info apod


        self.mars_content_action.triggered.connect(self.load_mars_content) #accion para ver contenido mars
        self.mars_about_action.triggered.connect(self.show_mars_info) #accion para ver


        self.neo_content_action.triggered.connect(self.load_neo_content) #accion para ver contenido neo
        self.neo_about_action.triggered.connect(self.show_neo_info) #accion para ver info neo


        self.notes_content_action.triggered.connect(self.load_notes_content) #accion para ver contenido notes
        self.notes_about_action.triggered.connect(self.show_notes_info) #accion para ver info notes


    def load_apod_content(self):
        pass

    def show_apod_info(self):
        QMessageBox.information(self, '¿Qué es APOD?', 'APOD (Astronomy Picture Of the Day) es un servicio de la NASA que publica diariamente desde 1995 una imagen o fotografía diferente del universo, con una breve explicación escrita por profesionales de la NASA. Incluye fotos de galaxias, nebulosas, planetas, eventos astronomicos y fenomenos cósmicos. Todo es con un fin educativo.')
        return

    def load_mars_content(self):
        pass

    def show_mars_info(self):
        QMessageBox.information(self, '¿Qué es Mars Rover Photos?', 'Mars Rover Photos es un servicio de la Nasa en la que se accede a fotografias tomadas por rovers(vehículos exploradores) que estuvieron o estan en Marte. Tienen diferentes rovers (en este caso Curiosity porque es el mas conocido activo en el momento). Todo es con un fin educativo para conocer mas sobre Marte y sus características.')
        return

    def load_neo_content(self):
        pass

    def show_neo_info(self):
        QMessageBox.information(self, '¿Qué es NEO?', 'NEO (Near Earth Objetcs) es un servicio de la NASA en la que accedemos informacion de los objetos cercanos a la Tierra, como asteroides y cometas. Los clasifica en potencialmente peligrosos o no peligrosos, también segun su tamaño. Todo es con un fin educativo para conocer mas sobre lo que sucede en la órbita terrestre.')
        return

    def load_notes_content(self):
        pass

    def show_notes_info(self):
        QMessageBox.information(self, '¿Qué es Notes?', 'Notes sirve para que el usuario tome notas de cosas de su interes, sobre el servicio que desee, esto se guardara y cada vez que entre con su usuario podra ver sus anotaciones y manipularlas a su gusto.')
        return

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
    

    def test(self):
        print("=== DEBUGGING ===\n")
        
        # Debug APOD
        print("1. Debug APOD...")
        try:
            url = f'{self.api._url}/planetary/apod'
            params = {'api_key': self.api._api_key}
            response = requests.get(url, params=params)
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "="*50 + "\n")
        
        # Debug Mars
        print("2. Debug Mars Photos...")
        try:
            url = f'{self.api._url}/mars-photos/api/v1/rovers/curiosity/photos'
            params = {'api_key': self.api._api_key, 'sol': 1000}
            response = requests.get(url, params=params)
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
        except Exception as e:
            print(f"Error: {e}")