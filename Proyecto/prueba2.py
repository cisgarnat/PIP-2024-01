import sys
from PyQt5 import uic, QtWidgets,QtCore
from Proyecto import prueba, prueba3

qtCreatorFile3 = "Menu.ui"
Ui_MainWindow,QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Jugar.clicked.connect(self.iniciar)
        self.btn_Personalizar.clicked.connect(self.pers)

        # Área de los Slots
    def iniciar(self):

        self.dialog= prueba.MyDialog()
        self.dialog.setModal(True)
        self.dialog.show()

    def pers(self):

        self.dialog = prueba3.MyDialogP()
        self.dialog.setModal(True)
        self.dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
###################################################3

