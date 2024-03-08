import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P14_QuestionarioP.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_lexiss.clicked.connect(self.clic_lexiss)
        self.rb_lexiss.toggled.connect(self.toggle_lexiss)
    # Área de los Slots

    def clic_lexiss(self):
        print("lexiss")
    def toggle_lexiss(self):

        estado = self.rb_lexiss.isChecked()
        print("lex cambio estado. Nuevo estado: {estado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

