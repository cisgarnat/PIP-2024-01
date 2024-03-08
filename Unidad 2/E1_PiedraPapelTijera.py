import sys
import random
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "E1_PiedraPapelTijera.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_Piedra.clicked.connect(self.juego)
        self.btn_Papel.clicked.connect(self.juego)
        self.btn_Tijera.clicked.connect(self.juego)

        self.txt_ganador.setEnabled(False)


    # Área de los Slots
    def juego(self):
        objeto = self.sender()
        nombre = objeto.objectName()


        if nombre == "btn_Piedra":
            self.img_jugador.setPixmap(QtGui.QPixmap(":/E1/Imagenes/piedra.jpg"))
            self.maquina()
        if nombre == "btn_Papel":
            self.img_jugador.setPixmap(QtGui.QPixmap(":/E1/Imagenes/papel.jpg"))
            self.maquina()
        if nombre == "btn_Tijera":
            self.img_jugador.setPixmap(QtGui.QPixmap(":/E1/Imagenes/tijeras.jpg"))
            self.maquina()


    def maquina(self):
        objeto = self.sender()
        maq = random.randint(1, 3)

        if maq == 1:
            self.img_maquina.setPixmap(QtGui.QPixmap(":/E1/Imagenes/piedra.jpg"))
            self.ganador(maq, objeto.objectName())
        if maq == 2:
            self.img_maquina.setPixmap(QtGui.QPixmap(":/E1/Imagenes/papel.jpg"))
            self.ganador(maq, objeto.objectName())
        if maq == 3:
            self.img_maquina.setPixmap(QtGui.QPixmap(":/E1/Imagenes/tijeras.jpg"))
            self.ganador(maq, objeto.objectName())



    def ganador(self, maq,nombre):

        if maq == 1 and nombre =="btn_Piedra":
            self.txt_ganador.setText("Empate")
        if maq == 1 and nombre == "btn_Papel":
            self.txt_ganador.setText("Gana Jugador")
        if maq == 1 and nombre == "btn_Tijera":
            self.txt_ganador.setText("Gana Maquina")
        if maq == 2 and nombre =="btn_Piedra":
            self.txt_ganador.setText("Gana Maquina")
        if maq == 2 and nombre == "btn_Papel":
            self.txt_ganador.setText("empate")
        if maq == 2 and nombre == "btn_Tijera":
            self.txt_ganador.setText("Gana Jugador")
        if maq == 3 and nombre =="btn_Piedra":
            self.txt_ganador.setText("Gana Jugador")
        if maq == 3 and nombre == "btn_Papel":
            self.txt_ganador.setText("Gana Maquina")
        if maq == 3 and nombre == "btn_Tijera":
            self.txt_ganador.setText("Empate")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

