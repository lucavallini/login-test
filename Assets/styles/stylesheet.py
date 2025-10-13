from PyQt5.QtWidgets import QLineEdit ,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont ,QIcon
from Assets.windows.widget_register import uiRegister
from Assets.windows.widget_login import uiLogin
from Assets.windows.main_window import uiMainWindow
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




class mainWindowStyle(uiMainWindow):
    def __init__(self):
        super().__init__()

        self._fav_label.setAlignment(Qt.AlignLeft)

        self.setWindowIcon(QIcon('Assets/icons/main_icon.png'))

        self.setStyleSheet('''
        QMainWindow{
            background-color: #000000;
        }

        QPushButton{
        background-color:#1d9bf0;
        border: 2px solid #1d9bf0;
        border-radius : 16px;        
        color : #ffffff;
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

        QLabel{
        color : #ffffff;
        font-weight: bold;
        font-size: 16px;
        margin:10px;
        padding:15px;
        }

        QMessageBox{
        background-color: #000000;
        color: #ffffff;
        font-weight: bold;
        font-size: 16px;
        }
        ''')
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = mainWindowStyle()
    main_window.show()
    sys.exit(app.exec_())
        