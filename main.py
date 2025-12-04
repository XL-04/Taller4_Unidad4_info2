from PyQt5.QtWidgets import QApplication
import sys
from controller.controlador import Controlador

if __name__ == "__main__":
    print(">>> INICIANDO LA APLICACIÓN...")
    
    app = QApplication(sys.argv)
    control = Controlador()
    
    sys.exit(app.exec_())
