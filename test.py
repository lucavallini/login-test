from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QLineEdit, QTextEdit, QWidget, 
                             QScrollArea, QComboBox)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import sys
import json
from api.nasa_api import nasaApi  # Asegúrate de que la ruta sea correcta

class NASAImageWidget(QWidget):
    def __init__(self, nasa_api):
        super().__init__()
        self.nasa_api = nasa_api
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_image_downloaded)
        self.current_reply = None
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Controles
        controls_layout = QHBoxLayout()
        self.btn_apod = QPushButton("Imagen del Día")
        self.btn_mars = QPushButton("Fotos de Marte")
        self.btn_neo = QPushButton("Asteroides")
        
        controls_layout.addWidget(self.btn_apod)
        controls_layout.addWidget(self.btn_mars)
        controls_layout.addWidget(self.btn_neo)
        
        # Área de visualización
        self.scroll_area = QScrollArea()
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setWidgetResizable(True)
        
        # Información de texto
        self.info_text = QTextEdit()
        self.info_text.setMaximumHeight(150)
        
        layout.addLayout(controls_layout)
        layout.addWidget(self.info_text)
        layout.addWidget(self.scroll_area)
        
        self.setLayout(layout)
        
        # Conectar botones
        self.btn_apod.clicked.connect(self.load_apod)
        self.btn_mars.clicked.connect(self.load_mars_photos)
        self.btn_neo.clicked.connect(self.load_neo_list)
    
    def clear_layout(self):
        """Limpiar el layout de imágenes anteriores"""
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def download_image(self, url):
        """Descargar imagen desde URL"""
        if self.current_reply:
            self.current_reply.abort()
        
        request = QNetworkRequest(QUrl(url))
        self.current_reply = self.network_manager.get(request)
    
    def on_image_downloaded(self, reply):
        """Cuando la imagen se descarga"""
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            image = QImage()
            image.loadFromData(data)
            
            pixmap = QPixmap(image)
            if not pixmap.isNull():
                # Crear widget para mostrar imagen
                image_widget = QLabel()
                image_widget.setPixmap(pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                image_widget.setAlignment(Qt.AlignCenter)
                image_widget.setStyleSheet("border: 1px solid gray; margin: 5px;")
                
                self.scroll_layout.addWidget(image_widget)
        
        reply.deleteLater()
        self.current_reply = None
    
    def load_apod(self):
        """Cargar Astronomy Picture of the Day"""
        self.clear_layout()
        self.info_text.clear()
        
        data = self.nasa_api.getApod()
        if data:
            self.info_text.setText(f"<b>Título:</b> {data.get('title', 'N/A')}\n"
                                  f"<b>Fecha:</b> {data.get('date', 'N/A')}\n"
                                  f"<b>Explicación:</b> {data.get('explanation', 'N/A')[:500]}...")
            
            if 'url' in data:
                self.download_image(data['url'])
        else:
            self.info_text.setText("Error al cargar APOD")
    
    def load_mars_photos(self):
        """Cargar fotos de Marte"""
        self.clear_layout()
        self.info_text.clear()
        
        data = self.nasa_api.getMars_photo(sol=1000)
        if data and 'photos' in data and data['photos']:
            photos = data['photos'][:10]  # Mostrar solo las primeras 10
            
            self.info_text.setText(f"Se encontraron {len(data['photos'])} fotos. Mostrando {len(photos)}")
            
            for photo in photos:
                if 'img_src' in photo:
                    self.download_image(photo['img_src'])
                    
                    # Agregar información de la foto
                    info_label = QLabel(f"Cámara: {photo.get('camera', {}).get('full_name', 'N/A')} | "
                                       f"Fecha terrestre: {photo.get('earth_date', 'N/A')}")
                    self.scroll_layout.addWidget(info_label)
        else:
            self.info_text.setText("No se encontraron fotos de Marte")
    
    def load_neo_list(self):
        """Cargar lista de asteroides"""
        self.clear_layout()
        self.info_text.clear()
        
        # Usar fecha de hoy y mañana como rango
        from datetime import datetime, timedelta
        start_date = datetime.now().strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        
        data = self.nasa_api.getNeo_list(start_date, end_date)
        if data and 'near_earth_objects' in data:
            neo_info = "🌍 Asteroides cercanos a la Tierra:\n\n"
            
            for date, neos in data['near_earth_objects'].items():
                for neo in neos[:5]:  # Mostrar solo los primeros 5 de cada día
                    name = neo.get('name', 'N/A')
                    diameter_min = neo.get('estimated_diameter', {}).get('meters', {}).get('estimated_diameter_min', 0)
                    hazardous = "✅ POTENCIALMENTE PELIGROSO" if neo.get('is_potentially_hazardous_asteroid') else "⚪ No peligroso"
                    
                    neo_info += f"• {name}\n"
                    neo_info += f"  Diámetro: ~{diameter_min:.1f}m | {hazardous}\n"
                    neo_info += f"  Velocidad: {neo.get('close_approach_data', [{}])[0].get('relative_velocity', {}).get('kilometers_per_second', 'N/A')} km/s\n\n"
            
            self.info_text.setText(neo_info)
        else:
            self.info_text.setText("No se encontraron asteroides cercanos")

class MainWindow(QMainWindow):
    def __init__(self, nasa_api):
        super().__init__()
        self.nasa_api = nasa_api
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("NASA API Viewer")
        self.setGeometry(100, 100, 800, 700)
        
        main_widget = NASAImageWidget(self.nasa_api)
        self.setCentralWidget(main_widget)

# Uso
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Tu clase NASA API
    nasa_api = nasaApi()
    
    window = MainWindow(nasa_api)
    window.show()
    
    sys.exit(app.exec_())