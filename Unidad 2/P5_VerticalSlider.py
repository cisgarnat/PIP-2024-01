import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo = {
            1:["Lexiss", "Dibujar", 21, "o+ ", ":/Equipo/Imagenes/Lexiss.jpg"],
            2: ["Rodrigo", "Comer", 20, "o- ", ":/Equipo/Imagenes/Rodrigo.jpg"],
            3: ["Victor", "Cocinar", 20, "a+ ", ":/Equipo/Imagenes/Victor.jpg"],
            4: ["Natalia", "Genshin", 20, " a-", ":/Equipo/Imagenes/Natalia.jpg"]
        }

        self.vs_personas.setMinimum(1)
        self.vs_personas.setMaximum(4)
        self.vs_personas.setSingleStep(1)
        self.vs_personas.setValue(1)
        self.vs_personas.valueChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        try:
            dataClave = self.vs_personas.value()
            imagen = self.datos_equipo[dataClave][-1]
            self.img_persona.setPixmap(QtGui.QPixmap(imagen))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

