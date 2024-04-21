import self

import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile3 = "Main_RecepcionInfo.ui"
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

        self.dialog  = MyDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()

#########################

qtCreatorFile3 = "Second_RecepcionInfo.ui"
Ui_dialog,QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.acceso = rPrincipal
        self.btn_sumar.clicked.connect(self.sumar)
        # Área de los Slots

    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_a.text())

        r= a+ b
        print(r)
        self.acceso.txt_resultado.setText(str(r))

        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

