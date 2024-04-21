import self

from UI_to_Python import P2_Ejemplo
import sys
from PyQt5 import uic, QtWidgets,QtCore
class MyApp(QtWidgets.QMainWindow, P2_Ejemplo.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        P2_Ejemplo.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

        self.btn_nuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nuevo.setGeometry(QtCore.QRect(290,50,191,61))
        self.btn_nuevo.setObjectName("btn_nuevo")

        self.btn_nuevo.setText("NUEVO SALUDO")

        self.btn_nuevo.clicked.connect(self.saludar)
        # Área de los Slots
    def saludar(self):
        self.lineEdit.setText("hola mundo")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

