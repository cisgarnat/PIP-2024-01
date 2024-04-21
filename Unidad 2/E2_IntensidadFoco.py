import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E2_IntensidadFoco.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.sli_intensidad.setMinimum(0)
        self.sli_intensidad.setMaximum(255)
        self.sli_intensidad.setSingleStep(1)
        self.sli_intensidad.setValue(0)
        self.sli_intensidad.valueChanged.connect(self.cambiaIntensidad)
        self.sli_intensidad.setEnabled(False)
        self.btn_encender.clicked.connect(self.encender)

        self.R = 0
        self.G = 0
        self.B = 0

        # Área de los Slots

    def encender(self):
        if not self.sli_intensidad.isEnabled():
            self.sli_intensidad.setEnabled(True)
            self.sli_intensidad.setValue(255)
            self.R = 255
            self.G = 255
            self.B = 255
            estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
            self.foco.setStyleSheet(estilo)
        else:
            self.sli_intensidad.setEnabled(False)
            self.sli_intensidad.setValue(0)
            self.R = 0
            self.G = 0
            self.B = 0
            estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
            self.foco.setStyleSheet(estilo)

    def cambiaIntensidad(self):
        self.R = self.sli_intensidad.value()
        self.G = self.sli_intensidad.value()
        self.B = self.sli_intensidad.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.foco.setStyleSheet(estilo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

