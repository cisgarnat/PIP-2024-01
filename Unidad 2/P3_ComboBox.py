import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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
        self.combo_personas.addItem("Selecciona....", 0)
        self.combo_personas.addItem("Lexiss", 1)
        self.combo_personas.addItem("Rodrigo", 2)
        self.combo_personas.addItem("Victor", 3)
        self.combo_personas.addItem("Natalia", 4)

        self.combo_personas.currentIndexChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        print("Text:" + self.combo_personas.currentText())
        print("Index:" + str(self.combo_personas.currentIndex()))
        print("Data:" + str(self.combo_personas.currentData()))

        dataClave = self.combo_personas.currentData()
        imagen = self.datos_equipo[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

