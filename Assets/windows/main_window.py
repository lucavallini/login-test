from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMenuBar, QAction)
from PyQt5.QtCore import Qt

class uiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stern')
        self.setGeometry(560, 240, 800, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #layout principal, es el q contiene todo
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        #invocamos metodo para crear la barra del menu
        self.setMenu_bar()

        #Widget para que va a contener el contenido que saquemos de la api
        nasa_widget = QWidget()
        nasa_layout = QVBoxLayout()#layout para widget
        nasa_widget.setLayout(nasa_layout)
        
        #area donde se va a mostrar contenido extraido de la api
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()#layout para el area de contenido, va a agregar los contenidos de la api
        self.content_area.setLayout(self.content_layout)


        
        nasa_layout.addWidget(self.content_area)

        #widget de la barra de usuario y favoritos
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout()#su layout
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setMaximumWidth(250)

        #boton usuario
        self._user_button = QPushButton('Usuario')

        #su label
        self._fav_label = QLabel('Tus favoritos')

        #lista para ver favoritos
        self._fav_list = QListWidget()

        #agregamos al layout de la barra lateral
        sidebar_layout.addWidget(self._user_button)
        sidebar_layout.addWidget(self._fav_label)
        sidebar_layout.addWidget(self._fav_list)

        #agregamos el widget del contenedor de contenido de la nasa, y el widget de la barra laterarl al layout main
        main_layout.addWidget(nasa_widget, 75)#le pasamos para q ocupe el 75% del espacio de la ventana
        main_layout.addWidget(sidebar_widget, 25)# y el resto lo va a ocupar la barra lateral


    #funcion que crea la barra del menu
    def setMenu_bar(self):
        menu_bar = self.menuBar()# creamos la barra menu
        
        apod_menu = menu_bar.addMenu('APOD')#añadimos APOD
        self.apod_content_action = QAction('Ver APOD', self) #para ver el contenido
        self.apod_about_action = QAction('About', self) #about
        apod_menu.addAction(self.apod_content_action)#añadimos al menu
        apod_menu.addAction(self.apod_about_action)# añadimos al menu
        
        mars_menu = menu_bar.addMenu('MARS')#añadimos MARS
        self.mars_content_action = QAction('Ver Fotos de Marte', self)#para ver el contenido
        self.mars_about_action = QAction('About', self)#about
        mars_menu.addAction(self.mars_content_action)#añadimos al menu
        mars_menu.addAction(self.mars_about_action)
        
        neo_menu = menu_bar.addMenu('NEO')
        self.neo_content_action = QAction('Ver Asteroides', self)
        self.neo_about_action = QAction('About', self)
        neo_menu.addAction(self.neo_content_action)
        neo_menu.addAction(self.neo_about_action)
        
        notes_menu = menu_bar.addMenu('NOTES')
        self.notes_content_action = QAction('Ver Notas', self)
        self.notes_about_action = QAction('About', self)
        notes_menu.addAction(self.notes_content_action)
        notes_menu.addAction(self.notes_about_action)



