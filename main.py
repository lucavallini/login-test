import sys
from modules.logica_login import ventanaLogin
from PyQt5.QtWidgets import QApplication
from database.db_operations import DatabaseManager
from database.conexion import setTables, getConexion

def main():
    if __name__ == '__main__':
        setTables()  # Crear las tablas si no existen
        print("Iniciando app...")  # debug
        app = QApplication(sys.argv)
        ventana_log = ventanaLogin()
        ventana_log.show()
        sys.exit(app.exec_())

main()
