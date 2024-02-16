import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagenes.ui"  # Nombre del archivo aquí.
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

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.index_control = 1

        self.btn_atras.setEnabled(False)

    # Área de los Slots

    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_equipo[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            #change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
            self.btn_atras.setEnabled(False)
    def adelante(self):
        if self.index_control < 4:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_equipo[self.index_control]
            print(datos)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 4:
            self.btn_adelante.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

