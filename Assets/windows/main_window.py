from PyQt5.QtWidgets import QMainWindow,QWidget, QLabel,QListWidget, QLineEdit, QGridLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt
import sys

class uiMainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Stern')
        self.setGeometry(560, 240, 800, 600)
        layout = QGridLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        #inf del user
        self._user_button = QPushButton('Usuario')

        #Favoritos
        self._fav_label = QLabel('Tus favoritos')
        self._fav_list = QListWidget() 

        #añade los widgets al layout
        layout.addWidget(self._user_button, 0, 1, Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(self._fav_label, 1, 1, Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(self._fav_list, 2, 0, 1, 2, Qt.AlignRight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = uiMainWindow()
    main_window.show()
    sys.exit(app.exec_())