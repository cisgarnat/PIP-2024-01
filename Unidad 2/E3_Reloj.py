import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QTimeEdit

qtCreatorFile = "E3_Reloj.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lcd_reloj.setNumDigits(8)
        self.lcd_reloj.display(QTime.currentTime().toString("hh:mm"))

    # Área de los Slots
    def alarma(self):
       pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

