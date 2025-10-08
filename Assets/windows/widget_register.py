from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QPushButton
import sys

#Ventana de registro
class uiRegister(QWidget):
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

