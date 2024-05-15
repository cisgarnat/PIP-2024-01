import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P4_BLINK_LED.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

       #self.btn_control_led.clicked.connect(self.control_led)
        self.estado_led = 1

    #Area de Slots
    def control_led(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.estado_led == 0:
                self.btn_control_led.setText("PRENDER")
            else:
                self.btn_control_led.setText("APAGAR")
            val = "1" if self.estado_led == 1 else "0" + "\n"
            print(val)
            self.arduino.write(val.encode())
            self.estado_led = self.estado_led * -1

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.txt_estado.setText("CONECTADO")
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.txt_estado.setText("DESCONECTADO")
            self.btn_accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.txt_estado.setText("CONECTADO")
            self.btn_accion.setText("DESCONECTAR")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())