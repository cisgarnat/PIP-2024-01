import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.txt_equipo.setPlainText("hola \n mundo")
        #self.cb_lexiss.clicked.connect(self.set_lexiss)
        self.cb_lexiss.toggled.connect(self.set_lexiss)
        self.cb_rodrigo.toggled.connect(self.set_rodrigo)
        self.cb_victor.toggled.connect(self.set_victor)
        self.cb_natalia.toggled.connect(self.set_natalia)

        self.lexiss = ""
        self.rodrigo = ""
        self.victor = ""
        self.natalia = ""

    # Área de los Slots

    def set_lexiss(self):
        if self.cb_lexiss.isChecked():
            print("Lexiss True")
            self.lexiss = "Lexiss"
        else:
            print("Lexiss False")
            self.lexiss = ""
        self.txt_equipo.setPlainText(self.lexiss + self.rodrigo + self.victor + self.natalia)
    def set_rodrigo(self):
        if self.cb_rodrigo.isChecked():
            print("Rodrigo True")
            self.rodrigo = "Rodrigo"
        else:
            print("Rodrigo False")
            self.rodrigo = ""
        self.txt_equipo.setPlainText(self.lexiss + self.rodrigo + self.victor + self.natalia)
    def set_victor(self):
        if self.victor.isChecked():
            print("Victor True")
            self.victor = "Victor"
        else:
            print("Victor False")
            self.victor = ""
        self.txt_equipo.setPlainText(self.lexiss + self.rodrigo + self.victor + self.natalia)
    def set_natalia(self):
        if self.cb_natalia.isChecked():
            print("Natalia True")
            self.natalia = "Natalia"
        else:
            print("Natalia False")
            self.natalia = ""
        self.txt_equipo.setPlainText(self.lexiss + self.rodrigo + self.victor + self.natalia)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

