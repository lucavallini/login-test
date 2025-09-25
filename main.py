from modules.logica_interfaz import *
from PyQt5.QtWidgets import QApplication

def main():
    if __name__ == '__main__':
        print("Iniciando app...")  # debug
        app = QApplication(sys.argv)
        ventana_log = VentanaLogin()
        ventana_log.show()
        sys.exit(app.exec_())

main()
