from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
import sys


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
            