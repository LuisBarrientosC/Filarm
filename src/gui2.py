# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt4.QtGui import *
import cv2 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(700, 620)
        Form.setStyleSheet(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 190, 161, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 140, 161, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 90, 161, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 290, 21, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 330, 21, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 370, 21, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 410, 21, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(420, 450, 21, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(420, 490, 21, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(420, 530, 21, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 90, 101, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 570, 141, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 190, 101, 41))
        self.pushButton_6.setStyleSheet(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 140, 101, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(610, 290, 61, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(610, 330, 61, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(610, 370, 61, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(610, 530, 61, 25))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 490, 61, 25))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(610, 410, 61, 25))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(610, 450, 61, 25))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(440, 290, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider_2 = QtGui.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(440, 330, 160, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalSlider_3 = QtGui.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(440, 370, 160, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalSlider_4 = QtGui.QSlider(Form)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(440, 410, 160, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.horizontalSlider_5 = QtGui.QSlider(Form)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(440, 450, 160, 16))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName(_fromUtf8("horizontalSlider_5"))
        self.horizontalSlider_6 = QtGui.QSlider(Form)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(440, 530, 160, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName(_fromUtf8("horizontalSlider_6"))
        self.horizontalSlider_7 = QtGui.QSlider(Form)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(440, 490, 160, 16))
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName(_fromUtf8("horizontalSlider_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(200, 10, 341, 51))
        self.label_8.setStyleSheet(_fromUtf8("\n"
"font: 75 11pt \"Sans\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(440, 260, 221, 17))
        self.label_9.setStyleSheet(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(50, 90, 311, 261))
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.foto)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.video)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.posicioninicio)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modomanual)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modoautomatico)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.xbox)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.planear)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.valorJ1)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.valorJ2)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.valorJ3)
        QtCore.QObject.connect(self.lineEdit_8, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.J4)
        QtCore.QObject.connect(self.lineEdit_9, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.J5)
        QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.J6)
        QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.valorJ7)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J1)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")),self.J2)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J3)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J4)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J5)
        QtCore.QObject.connect(self.horizontalSlider_7, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J6)
        QtCore.QObject.connect(self.horizontalSlider_6, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J7)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Modo Manual", None))
        self.pushButton_2.setText(_translate("Form", "Modo Automatico", None))
        self.pushButton_3.setText(_translate("Form", "Posicion de inicio", None))
        self.label.setText(_translate("Form", "J1", None))
        self.label_2.setText(_translate("Form", "J2", None))
        self.label_3.setText(_translate("Form", "J3", None))
        self.label_4.setText(_translate("Form", "J4", None))
        self.label_5.setText(_translate("Form", "J5", None))
        self.label_6.setText(_translate("Form", "J6", None))
        self.label_7.setText(_translate("Form", "J7", None))
        self.pushButton_4.setText(_translate("Form", "XBOX", None))
        self.pushButton_5.setText(_translate("Form", "PLANEAR", None))
        self.pushButton_6.setText(_translate("Form", "Foto", None))
        self.pushButton_7.setText(_translate("Form", "VIdeo", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">FILMMAKER ROBOT ARM</span></p></body></html>", None))
        self.label_9.setText(_translate("Form", "Control de posicion de motores", None))
    #def foto(self):
     #   print ("Foto")

   # def video(self):
     #   print ("Video")

    def posicioninicio(self):
        print ("Video")
    
    def modomanual(self):
        print ("Modo manual_GUI")
    
    def xbox(self):
        print ("MODO_MANUAL_XBOX")
    
    def modoautomatico(self):
        self.xbox_status=2
        print ("Modo automatico")

    def planear(self):
        print ("PLANEAR") 

    def valorJ1(self):
        print ("J1")       

    def valorJ2(self):
        print ("J2")       

    def valorJ3(self):
        print ("J3")  

    def valorJ4(self):
        print ("J4")  

    def valorJ5(self):
        print ("J5")  

    def valorJ6(self):
        print ("J6")  

    def valorJ7(self):
        print ("J7")  
    
    def J1(self):
        print ("slider")

    def J2(self):
        print ("slider")

    def J3(self):
        print ("slider")

    def J4(self):
        print ("slider")

    def J5(self):
        print ("slider")

    def J6(self):
        print ("slider")

    def J7(self):
        print ("slider")
    #    float (self.M7)
    #    self.M7= (self.horizontalSlider_7.value())
    #    self.lineEdit_6.setText(str(self.M7))
    
    def foto(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)

    def Imageupd_slot(self, Image):
        self.label.setPixmap(QPixmap.fromImage(Image))

    def video(self):
        self.label.clear()
        self.Work.stop()

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(0)
        while self.hilo_corriendo:
            ret, frame = cap.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flip = cv2.flip(Image, 1)
                convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(320, 240, Qt.KeepAspectRatio)
                self.Imageupd.emit(pic)
    def stop(self):
        self.hilo_corriendo = False
        self.quit()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
