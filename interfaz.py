from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
import sys
import main



#Ventana de inicio sesion


class Ui_Login (QWidget):
    def __init__(self):
        super().__init__()#heredamos de la clase qwidget
        self.setWindowTitle('Inicio sesión')
        self.setGeometry(560, 240, 800, 600) #donde va abrirse la ventana


        layout = QGridLayout()
        self.setLayout(layout)

        self._title = QLabel('Inicia sesión')
        self._title.setAlignment(Qt.AlignCenter)

        #Usuario 
        self._user_label = QLabel ('User: ')
        self._user_input = QLineEdit()

        #Contraseña
        self._password_label = QLabel('Password: ')
        self._password_input = QLineEdit()

        #boton para loguearse
        self._login_button = QPushButton ('Login')

        #boton registrarse
        self._register_label = QLabel('¿No tenes cuenta?')
        self._register_button = QPushButton('Registrate')

        #Agregamos widgets
        layout.addWidget(self._title, 0, 0, 1, 2)

        #Widgets usuario
        layout.addWidget(self._user_label, 1, 0)
        layout.addWidget(self._user_input, 1, 1)

        #Widgets password
        layout.addWidget(self._password_label, 2, 0)
        layout.addWidget(self._password_input, 2, 1)

        #Widget login
        layout.addWidget(self._login_button, 3, 1)

        #widget register
        layout.addWidget(self._register_label, 4, 0)
        layout.addWidget(self._register_button, 4, 1)
            


#Ventana de registro

class Ui_Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Register')
        self.setGeometry(560, 240, 800, 600)
        layout = QGridLayout()
        self.setLayout(layout)


        #titulo
        self._title_reg = QLabel ('Unete a nuestra comunidad')


        #usuario
        self._user_label_reg= QLabel('Ingrese su usuario: ')
        self._user_input_reg = QLineEdit ()
        
        #password
        self._password_label_reg= QLabel('Elija su contraseña: ')
        self._password_input_reg = QLineEdit()

        #password cheCk
        self._password_label_reg_verify = QLabel('Confirma tu contraseña: ')
        self._password_input_reg_verify = QLineEdit()

        #register button
        self._register_button = QPushButton('¡Registrate ahora!')

        #title widget
        layout.addWidget(self._title_reg, 0, 0 , 1, 2)

        #user widget
        layout.addWidget(self._user_label_reg, 1, 0)
        layout.addWidget(self._user_input_reg, 1, 1)

        #password widget
        layout.addWidget(self._password_label_reg, 2, 0)
        layout.addWidget(self._password_input_reg, 2, 1)

        #password checl widget
        layout.addWidget(self._password_label_reg_verify, 3, 0)
        layout.addWidget(self._password_input_reg_verify, 3, 1)

        #register button widget
        layout.addWidget(self._register_button, 4,1)

