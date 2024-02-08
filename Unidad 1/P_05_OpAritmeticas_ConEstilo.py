import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmaticas_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.operacion)
        self.btn_restar.clicked.connect(self.operacion)
        self.btn_multi.clicked.connect(self.operacion)
        self.btn_division.clicked.connect(self.operacion)
        self.txt_resultado.setEnabled(False)
    # Área de los Slots
    def operacion(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()
            print(nombre)
            A = int(self.txt_A.text())
            B = int(self.txt_B.text())

            if nombre == "btn_suma":
                r = A+B
            elif nombre == "btn_restar":
                r = A-B
            elif nombre == "btn_multi":
                r = A*B
            else:
                r = A/B

            self.txt_resultado.setText(str(r))
        except Exception as error:
            print(error)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

