# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plantilla_Juego.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(989, 533)
        Dialog.setStyleSheet("background-color: rgb(43, 58, 196);")
        self.btn_izquierda = QtWidgets.QPushButton(Dialog)
        self.btn_izquierda.setGeometry(QtCore.QRect(580, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_izquierda.setFont(font)
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.btn_abajo = QtWidgets.QPushButton(Dialog)
        self.btn_abajo.setGeometry(QtCore.QRect(720, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abajo.setFont(font)
        self.btn_abajo.setObjectName("btn_abajo")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 501, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_arriba = QtWidgets.QPushButton(Dialog)
        self.btn_arriba.setGeometry(QtCore.QRect(720, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_arriba.setFont(font)
        self.btn_arriba.setObjectName("btn_arriba")
        self.btn_centro = QtWidgets.QPushButton(Dialog)
        self.btn_centro.setGeometry(QtCore.QRect(720, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_centro.setFont(font)
        self.btn_centro.setObjectName("btn_centro")
        self.btn_derecha = QtWidgets.QPushButton(Dialog)
        self.btn_derecha.setGeometry(QtCore.QRect(860, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_derecha.setFont(font)
        self.btn_derecha.setObjectName("btn_derecha")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(860, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(720, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(580, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Score = QtWidgets.QLineEdit(Dialog)
        self.Score.setGeometry(QtCore.QRect(580, 70, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.Score.setFont(font)
        self.Score.setObjectName("Score")
        self.Vidas = QtWidgets.QLineEdit(Dialog)
        self.Vidas.setGeometry(QtCore.QRect(720, 70, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.Vidas.setFont(font)
        self.Vidas.setObjectName("Vidas")
        self.Tiempo = QtWidgets.QLineEdit(Dialog)
        self.Tiempo.setGeometry(QtCore.QRect(860, 70, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.Tiempo.setFont(font)
        self.Tiempo.setObjectName("Tiempo")

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)
        # para referir al mismo axes

        self.verticalLayout.addWidget(self.canvas)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_izquierda.setText(_translate("Dialog", "IZQUIERDA"))
        self.btn_abajo.setText(_translate("Dialog", "ABAJO"))
        self.btn_arriba.setText(_translate("Dialog", "ARRIBA"))
        self.btn_centro.setText(_translate("Dialog", "CENTRO"))
        self.btn_derecha.setText(_translate("Dialog", "DERECHA"))
        self.label.setText(_translate("Dialog", "Tiempo"))
        self.label_2.setText(_translate("Dialog", "Vidas"))
        self.label_3.setText(_translate("Dialog", "Score"))
