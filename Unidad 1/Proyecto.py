import sys
from PyQt5 import uic, QtWidgets
import statistics
qtCreatorFile = ("Proyecto.ui")  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_valorMayor.clicked.connect(self.operacion)
        self.btn_valorMenor.clicked.connect(self.operacion)
        self.btn_media.clicked.connect(self.operacion)
        self.btn_mediana.clicked.connect(self.operacion)
        self.btn_moda.clicked.connect(self.operacion)
        self.btn_desviacionEstandar.clicked.connect(self.operacion)
        self.btn_varianza.clicked.connect(self.operacion)
        self.txt_resultado.setEnabled(False)
    # Área de los Slots

    def operacion(self):

        try:
            numeros = self.txt_numeros.text()
            lista = numeros.split(" ")
            lista_en_numeros = [int(i) for i in lista]
            objeto = self.sender()
            nombre = objeto.objectName()

            if nombre == "btn_valorMayor":
                r = max(lista_en_numeros)
            elif nombre == "btn_valorMenor":
                r = min(lista_en_numeros)
            elif nombre == "btn_media":
                r = statistics.mean(lista_en_numeros)
            elif nombre == "btn_mediana":
                r = statistics.median(lista_en_numeros)
            elif nombre == "btn_moda":
                r = statistics.mode(lista_en_numeros)
            elif nombre == "btn_desviacionEstandar":
                r = statistics.stdev(lista_en_numeros)
            else:
                r = statistics.variance(lista_en_numeros)


            self.txt_resultado.setText(str(r))
        except Exception as error:
            print(error)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

