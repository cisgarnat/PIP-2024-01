
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

qtCreatorFile3 = "Personalizar.ui"
Ui_dialog,QtBaseClass3 = uic.loadUiType(qtCreatorFile3)
class MyDialogP(QtWidgets.QDialog, Ui_dialog):
    info_signal = pyqtSignal(str)
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion

        self.btn_aceptar.clicked.connect(self.enviar)
        self.rbtn_amarillo.clicked.connect(self.color)
        self.rbtn_rojo.clicked.connect(self.color)
        self.rbtn_naranja.clicked.connect(self.color)
        self.rbtn_morado.clicked.connect(self.color)
        self.color = "yellow"
    def color(self):
        objeto = self.sender()
        nombre = objeto.objectName()

        if nombre == "rbtn_amarillo":
            self.color = "yellow"
        elif nombre == "rbtn_rojo":
            self.color = "red"
        elif nombre == "rbtn_naranja":
            self.color = "orange"
        else :
            self.color = "purple"

    def enviar(self):
        self.hide()



