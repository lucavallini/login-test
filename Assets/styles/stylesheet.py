from PyQt5.QtWidgets import QLineEdit ,QApplication, QLabel, QSizePolicy, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont ,QIcon , QMovie
from PyQt5 import QtWidgets
from Assets.windows.widget_register import uiRegister
from Assets.windows.widget_login import uiLogin
from Assets.windows.main_window import uiWert
import sys
import os



# Stylesheet de los dos widget (falta agregar una ventana principal)
# Todos los colores en hex, siguiendo palte de colores negro, blanco, azul

class loginStyle(uiLogin):
    def __init__(self):
        super().__init__()

        self._title.setAlignment(Qt.AlignCenter)

        self._user_label.setAlignment(Qt.AlignCenter)
        self._user_input.setAlignment(Qt.AlignCenter)

        self._password_label.setAlignment(Qt.AlignCenter)
        self._password_input.setAlignment(Qt.AlignCenter)
        self._password_input.setEchoMode(QLineEdit.Password)
        
        self._title.setStyleSheet("font-size: 46px; font-weight: bold; color: #1A3300;")

        self.setWindowIcon(QIcon('Assets/icons/icon.png'))

        self.setStyleSheet(''' 
        QWidget{
            background-color: #ffffff;
        }
        
        
        QLabel{
            color : #1A3300;
            font-weight: bold;
            font-size: 16px;
            margin:10px;
            padding:15px;
        }
        QPushButton{
            background-color:#1A3300;
            border: 2px solid #1A3300;
            border-radius : 16px;        
            color : #ffffff;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }
        
        QLineEdit{
        border: 2px solid #1A3300;
        border-radius : 8px;
        color : #000000;
        margin:10px;
        padding:15px;
        }
        
        ''')



class registerStyle(uiRegister):
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

        self._title_reg.setStyleSheet("font-size: 46px; font-weight: bold; color: #1A3300;")
        
        self.setWindowIcon(QIcon('Assets/icons/icon.png'))

        self.setStyleSheet(''' 
        QWidget{
            background-color: #fffffff;
        }
        
        
        QLabel{
            color : #1A3300;
            font-weight: bold;
            font-size: 16px;
            margin:10px;
            padding:15px;
        }
        QPushButton{
            background-color:#1A3300;
            border: 2px solid #1A3300;
            border-radius : 16px;        
            color : #ffffff;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }
        
        QLineEdit{
        border: 2px solid #1A3300;
        border-radius : 8px;
        color : #000000;
        margin:10px;
        padding:15px;
        }
        
        ''')



class mainWindowStyle(QMainWindow):
    def __init__(self):
        super().__init__()

        
        # Crear instancia de la UI generada
        self.ui = uiWert()
        self.ui.setupUi(self)  # Configurar la UI en esta ventana
        
        # Establecer ícono
        self.setWindowIcon(QIcon('Assets/icons/main_wert_icon.png'))

        self.setStyleSheet('''
        QMessageBox{
            background-color:#ffffff;
            border-radius : 16px;        
            color : #1a3300;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }

        QMessageBox QPushButton{
            background-color:#1A3300;
            border: 2px solid #1A3300;
            border-radius : 16px;        
            color : #ffffff;
            font-weight : bold;
            font-size: 14px;
            margin:10px;
            padding:15px;
        }
        ''')
