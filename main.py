from modules.logica_interfaz import *
from PyQt5.QtWidgets import QApplication
from database.conexion import createDatabase

def main():
    if __name__ == '__main__':
        createDatabase()  # Crear la base de datos si no existe
        print("Iniciando app...")  # debug
        app = QApplication(sys.argv)
        ventana_log = ventanaLogin()
        ventana_log.show()
        sys.exit(app.exec_())

main()
