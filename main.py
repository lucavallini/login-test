from modules.logica_interfaz import *
from PyQt5.QtWidgets import QApplication
from database.db_operations import DatabaseManager
from database.conexion import createTable, getConexion

def main():
    if __name__ == '__main__':
        createTable(None)  # Crear la tabla si no existe
        print("Iniciando app...")  # debug
        app = QApplication(sys.argv)
        ventana_log = ventanaLogin()
        ventana_log.show()
        sys.exit(app.exec_())

main()
