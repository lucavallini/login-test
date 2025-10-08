from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont ,QIcon
from Assets.ui_register import Ui_Register
from Assets.ui_login import Ui_Login
import sys
import os


# Stylesheet de los dos widget (falta agregar una ventana principal)
# Todos los colores en hex, siguiendo palte de colores negro, blanco, azul

class LoginStyle(Ui_Login):
    def __init__(self):
        super().__init__()

        self._title.setAlignment(Qt.AlignCenter)

        self._user_label.setAlignment(Qt.AlignCenter)
        self._user_input.setAlignment(Qt.AlignCenter)

        self._password_label.setAlignment(Qt.AlignCenter)
        self._password_input.setAlignment(Qt.AlignCenter)
        self._password_input.setEchoMode(QLineEdit.Password)
        
        self._title.setStyleSheet("font-size: 46px; font-weight: bold; color: white;")

        self.setWindowIcon(QIcon('Assets/icons/icon.png'))

        self.setStyleSheet(''' 
        QWidget{
            background-color: #000000;
        }
        
        
        QLabel{
            color : #ffffff;
            font-weight: bold;
            font-size: 16px;
            margin:10px;
            padding:15px;
        }
        QPushButton{
            background-color:#ffffff;
            border: 2px solid #ffffff;
            border-radius : 16px;        
            color : #000000;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }
        
        QLineEdit{
        border: 2px solid #1d9bf0;
        border-radius : 8px;
        color : #ffffff;
        margin:10px;
        padding:15px;
        }
        
        ''')



class RegisterStyle(Ui_Register):
    def __init__(self):
        super().__init__()

        self._title_reg.setAlignment(Qt.AlignCenter)

        self._user_label_reg.setAlignment(Qt.AlignCenter)
        self._user_input_reg.setAlignment(Qt.AlignCenter)

        self._password_label_reg.setAlignment(Qt.AlignCenter)
        self._password_input_reg.setAlignment(Qt.AlignCenter)
        self._password_input_reg.setEchoMode(QLineEdit.Password)

        self._password_label_reg_verify.setAlignment(Qt.AlignCenter)
        self._password_input_reg_verify.setAlignment(Qt.AlignCenter)
        self._password_input_reg_verify.setEchoMode(QLineEdit.Password)

        self._title_reg.setStyleSheet("font-size: 46px; font-weight: bold; color: white;")
        
        self.setWindowIcon(QIcon('Assets/icons/icon.png'))

        self.setStyleSheet(''' 
        QWidget{
            background-color: #000000;
        }
        
        
        QLabel{
            color : #ffffff;
            font-weight: bold;
            font-size: 16px;
            margin:10px;
            padding:15px;
        }
        QPushButton{
            background-color:#ffffff;
            border: 2px solid #ffffff;
            border-radius : 16px;        
            color : #000000;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }
        
        QLineEdit{
        border: 2px solid #1d9bf0;
        border-radius : 8px;
        color : #ffffff;
        margin:10px;
        padding:15px;
        }
        
        ''')




