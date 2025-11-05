import sys
from PyQt5.QtWidgets import QMessageBox, QTextEdit
import requests
from Assets.styles.stylesheet import registerStyle, loginStyle, mainWindowStyle
from database.conexion import getConexion
from database.db_operations import DatabaseManager
from api.world_bank_api import WorldBankAPI
from api.currency_api import RateAPi

class ventanaMain(mainWindowStyle): #ventana principal, despues de loguearse
    def __init__(self, db_manager, user): #hereda la instancia de db_manager
        super().__init__()

        country= self.ui.pais_combo.currentText()
        print (country)
        self.db_manager = db_manager #instanciamos
        self.user = user
        self.id = self.db_manager.getId(user)[0]  # Obtener el ID del usuario actual
        self.apiwb = WorldBankAPI()  # Instancia de la clase WorldBankAPI
        

        self.get_note_titles()  # Cargar los títulos de las notas al iniciar la ventana principal
        self.get_countries_names()  # Cargar los nombres de los países al iniciar la ventana principal
        self.get_indicators_names()


        # configuracion de botones del menu
        self.ui.action_view_rates_action.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.action_view_data.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.action_view_notes.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        #botones
        self.ui.user_button.clicked.connect(self.show_user_info)

        #change btns
        self.ui.convertir_button.clicked.connect(self.show_convert_currency)

        #eco bttns
        self.ui.datos_button.clicked.connect(self.show_economic_data)

        #notes bttns
        self.ui.cargar_nota_button.clicked.connect(self.load_note)
        self.ui.guardar_button.clicked.connect(self.save_note)
        self.ui.eliminar_button.clicked.connect(self.delete_note)
        self.ui.nueva_button.clicked.connect(self.new_note)

    def show_user_info(self):
        QMessageBox.information(self, 'Current User', f'Sesion actual: {self.user}')
        return
    
    def show_convert_currency(self):
        pass
    
    def get_countries_names(self):
        paises = self.apiwb.get_countries()
        if paises:
            for codigo, pais in paises:
                self.ui.pais_combo.addItem(f'{pais} ({codigo})', codigo)
    
    def get_indicators_names(self):
        indicators = self.apiwb.get_indicators()
        if indicators:
            for cod, indicator in indicators.items():
                self.ui.indicador_combo.addItem(f'{indicator}', cod)

    def show_economic_data(self):
        indicador = self.ui.indicador_combo.currentData()
        pais = self.ui.pais_combo.currentData()
        consulta = self.apiwb.get_eco_info(pais, indicador)
        text = self.apiwb.format_eco_data(consulta)
        self.ui.datos_text.setText(text)


    def load_note(self):
        note = self.db_manager.getNoteContent(self.id, self.ui.notas_combo.currentText())
        if note:
            self.ui.nota_input.setPlainText(note[0])
            self.ui.titulo_nota_input.setText(self.ui.notas_combo.currentText())
            self.ui.titulo_nota_input.setReadOnly(True) 
        else:
            QMessageBox.critical(self, 'Error', 'Error al cargar la nota.')


    def save_note(self):
        titulo = self.ui.titulo_nota_input.text()
        nota = self.ui.nota_input.toPlainText()
        if not titulo or not nota:
            QMessageBox.critical(self, 'Error', 'Rellene los campos de titulo y nota antes de guardar.')
            return
        
        else:
            try:
                self.db_manager.setNote(self.id, titulo, nota)
                QMessageBox.information(self, 'Exito', 'Nota guardada correctamente.')
                self.ui.notas_combo.clear()
                self.get_note_titles()  # Actualizar la lista de títulos después de guardar una nota
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al guardar la nota: {str(e)}')

    def delete_note(self):
        titulo = self.ui.notas_combo.currentText()
        if not titulo:
            QMessageBox.critical(self, 'Error', 'Seleccione una nota para eliminar.')
            return
        
        try:
            self.db_manager.deleteNote(self.id, titulo)
            QMessageBox.information(self, 'Exito', 'Nota eliminada correctamente.')
            self.ui.nota_input.clear()
            self.ui.titulo_nota_input.clear()
            self.ui.notas_combo.clear()
            self.get_note_titles()  # Actualizar la lista de títulos después de eliminar una nota
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al eliminar la nota: {str(e)}')


    def new_note(self):
        self.ui.nota_input.clear()
        self.ui.titulo_nota_input.clear()
        self.ui.titulo_nota_input.setReadOnly(False)

    def get_note_titles(self):
        titles = self.db_manager.getTitles(self.id)
        for title in titles:
            self.ui.notas_combo.addItem(title[0])