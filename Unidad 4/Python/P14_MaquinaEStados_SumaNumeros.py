import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P14_MaquinaEStados_SumaNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)
        self.btn_enviar.clicked.connect(self.lecturaArduino)


    #Area de Slots
    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                a = self.txt_a.text()
                b = self.txt_b.text()
                self.arduino.write(a.encode('utf-8'))
                self.arduino.write(b.encode('utf-8'))
                r = self.arduino.readline()
                r = r.decode()
                r = r.strip()
                self.txt_r.setText(r)
                if r != "":
                    self.datos.addItem(r)
                    self.datos.setCurrentRow(self.datos.count()-1)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())