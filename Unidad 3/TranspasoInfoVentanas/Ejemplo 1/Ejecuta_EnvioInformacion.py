import self

import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile3 = "Main_EnvioInfo.ui"
Ui_MainWindow,QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

        # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        r = a+ b
        self.dialog  = MyDialog()
        self.dialog.setModal(True)
        self.dialog.txt_resultado.setText(str(r))
        self.dialog.show()

#########################

qtCreatorFile3 = "Second_EnvioInfo.ui"
Ui_dialog,QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        # Área de los Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

