# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String, Float32
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from Trayectoria2 import *

global M11,M21,M31,M41,M51,M61
global M12,M22,M32,M42,M52,M62
global M13,M23,M33,M43,M53,M63
global M14,M24,M34,M44,M54,M64



class Ui_trayectoria2(object):

    def setupUi(self, trayectoria2):
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group_name = "manipulator"
        self.move_group = moveit_commander.MoveGroupCommander(self.group_name)

        self.planning_frame = self.move_group.get_planning_frame()
        print("============ Planning frame: %s" % self.planning_frame)

        # We can also print the name of the end-effector link for this group:
        self.eef_link = self.move_group.get_end_effector_link()
        print("============ End effector link: %s" % self.eef_link)

        # We can get a list of all the groups in the robot:
        self.group_names = self.robot.get_group_names()
        print("============ Available Planning Groups:", self.robot.get_group_names())

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print("============ Printing robot state")
        print(self.robot.get_current_state())
        print("")
        
        self.M1=0.0
        self.M2=0.0
        self.M3=0.0
        self.M4=0.0
        self.M5=0.0
        self.M6=0.0

        self.M11=0.0
        self.M21=0.0
        self.M31=0.0
        self.M41=0.0
        self.M51=0.0
        self.M61=0.0

        self.M12=0.0
        self.M22=0.0
        self.M32=0.0
        self.M42=0.0
        self.M52=0.0
        self.M62=0.0

        self.M13=0.0
        self.M23=0.0
        self.M33=0.0
        self.M43=0.0
        self.M53=0.0
        self.M63=0.0

        self.M14=0.0
        self.M24=0.0
        self.M34=0.0
        self.M44=0.0
        self.M54=0.0
        self.M64=0.0

        self.Ac=0.1
        self.Ve=0.1
        self.Tm=0.5

        trayectoria2.setObjectName("trayectoria2")
        trayectoria2.resize(424, 464)
        self.pushButton = QtWidgets.QPushButton(trayectoria2)
        self.pushButton.setGeometry(QtCore.QRect(180, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(trayectoria2)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 21, 20))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(trayectoria2)
        self.label.setGeometry(QtCore.QRect(20, 70, 21, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(trayectoria2)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 21, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(trayectoria2)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 21, 20))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(trayectoria2)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 21, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(trayectoria2)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 21, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 270, 61, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_8.setGeometry(QtCore.QRect(40, 190, 61, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 61, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 150, 61, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_9.setGeometry(QtCore.QRect(40, 230, 61, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 61, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_13 = QtWidgets.QLabel(trayectoria2)
        self.label_13.setGeometry(QtCore.QRect(40, 50, 51, 17))
        self.label_13.setObjectName("label_13")
        self.pushButton_15 = QtWidgets.QPushButton(trayectoria2)
        self.pushButton_15.setGeometry(QtCore.QRect(50, 300, 41, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_7 = QtWidgets.QLabel(trayectoria2)
        self.label_7.setGeometry(QtCore.QRect(120, 230, 21, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_10.setGeometry(QtCore.QRect(140, 190, 61, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(trayectoria2)
        self.label_14.setGeometry(QtCore.QRect(140, 50, 51, 17))
        self.label_14.setObjectName("label_14")
        self.label_8 = QtWidgets.QLabel(trayectoria2)
        self.label_8.setGeometry(QtCore.QRect(120, 190, 21, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 110, 61, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 150, 61, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 230, 61, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_16 = QtWidgets.QPushButton(trayectoria2)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 300, 41, 21))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_9 = QtWidgets.QLabel(trayectoria2)
        self.label_9.setGeometry(QtCore.QRect(120, 270, 21, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 70, 61, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(trayectoria2)
        self.label_10.setGeometry(QtCore.QRect(120, 110, 21, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_12 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_12.setGeometry(QtCore.QRect(140, 270, 61, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_11 = QtWidgets.QLabel(trayectoria2)
        self.label_11.setGeometry(QtCore.QRect(120, 70, 21, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(trayectoria2)
        self.label_12.setGeometry(QtCore.QRect(120, 150, 21, 20))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(trayectoria2)
        self.label_15.setGeometry(QtCore.QRect(230, 190, 21, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_13 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_13.setGeometry(QtCore.QRect(250, 110, 61, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_14.setGeometry(QtCore.QRect(250, 70, 61, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_16 = QtWidgets.QLabel(trayectoria2)
        self.label_16.setGeometry(QtCore.QRect(230, 110, 21, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(trayectoria2)
        self.label_17.setGeometry(QtCore.QRect(230, 70, 21, 20))
        self.label_17.setObjectName("label_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_15.setGeometry(QtCore.QRect(250, 270, 61, 25))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_18 = QtWidgets.QLabel(trayectoria2)
        self.label_18.setGeometry(QtCore.QRect(250, 50, 51, 17))
        self.label_18.setObjectName("label_18")
        self.lineEdit_16 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 190, 61, 25))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_17.setGeometry(QtCore.QRect(250, 150, 61, 25))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_19 = QtWidgets.QLabel(trayectoria2)
        self.label_19.setGeometry(QtCore.QRect(230, 230, 21, 20))
        self.label_19.setObjectName("label_19")
        self.lineEdit_18 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_18.setGeometry(QtCore.QRect(250, 230, 61, 25))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_20 = QtWidgets.QLabel(trayectoria2)
        self.label_20.setGeometry(QtCore.QRect(230, 270, 21, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(trayectoria2)
        self.label_21.setGeometry(QtCore.QRect(230, 150, 21, 20))
        self.label_21.setObjectName("label_21")
        self.pushButton_17 = QtWidgets.QPushButton(trayectoria2)
        self.pushButton_17.setGeometry(QtCore.QRect(260, 300, 41, 21))
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_19 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_19.setGeometry(QtCore.QRect(230, 340, 61, 25))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_22 = QtWidgets.QLabel(trayectoria2)
        self.label_22.setGeometry(QtCore.QRect(20, 340, 211, 17))
        self.label_22.setObjectName("label_22")
        self.pushButton_18 = QtWidgets.QPushButton(trayectoria2)
        self.pushButton_18.setGeometry(QtCore.QRect(360, 300, 41, 21))
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_20 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_20.setGeometry(QtCore.QRect(350, 190, 61, 25))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_23 = QtWidgets.QLabel(trayectoria2)
        self.label_23.setGeometry(QtCore.QRect(330, 150, 21, 20))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(trayectoria2)
        self.label_24.setGeometry(QtCore.QRect(330, 110, 21, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(trayectoria2)
        self.label_25.setGeometry(QtCore.QRect(330, 230, 21, 20))
        self.label_25.setObjectName("label_25")
        self.lineEdit_21 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_21.setGeometry(QtCore.QRect(350, 70, 61, 25))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_26 = QtWidgets.QLabel(trayectoria2)
        self.label_26.setGeometry(QtCore.QRect(330, 70, 21, 20))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(trayectoria2)
        self.label_27.setGeometry(QtCore.QRect(330, 190, 21, 20))
        self.label_27.setObjectName("label_27")
        self.lineEdit_22 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_22.setGeometry(QtCore.QRect(350, 110, 61, 25))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_28 = QtWidgets.QLabel(trayectoria2)
        self.label_28.setGeometry(QtCore.QRect(330, 270, 21, 20))
        self.label_28.setObjectName("label_28")
        self.lineEdit_23 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_23.setGeometry(QtCore.QRect(350, 270, 61, 25))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_29 = QtWidgets.QLabel(trayectoria2)
        self.label_29.setGeometry(QtCore.QRect(350, 50, 51, 17))
        self.label_29.setObjectName("label_29")
        self.lineEdit_24 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_24.setGeometry(QtCore.QRect(350, 150, 61, 25))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_25.setGeometry(QtCore.QRect(350, 230, 61, 25))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_19 = QtWidgets.QPushButton(trayectoria2)
        self.pushButton_19.setGeometry(QtCore.QRect(330, 430, 81, 21))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_30 = QtWidgets.QLabel(trayectoria2)
        self.label_30.setGeometry(QtCore.QRect(20, 400, 111, 19))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(trayectoria2)
        self.label_31.setGeometry(QtCore.QRect(20, 370, 111, 19))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(trayectoria2)
        self.label_32.setGeometry(QtCore.QRect(210, 400, 79, 19))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(trayectoria2)
        self.label_33.setGeometry(QtCore.QRect(20, 430, 191, 19))
        self.label_33.setObjectName("label_33")
        self.lineEdit_26 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_26.setGeometry(QtCore.QRect(130, 400, 61, 25))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_34 = QtWidgets.QLabel(trayectoria2)
        self.label_34.setGeometry(QtCore.QRect(280, 430, 79, 21))
        self.label_34.setObjectName("label_34")
        self.lineEdit_27 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_27.setGeometry(QtCore.QRect(130, 370, 61, 25))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_35 = QtWidgets.QLabel(trayectoria2)
        self.label_35.setGeometry(QtCore.QRect(210, 370, 79, 19))
        self.label_35.setObjectName("label_35")
        self.lineEdit_28 = QtWidgets.QLineEdit(trayectoria2)
        self.lineEdit_28.setGeometry(QtCore.QRect(210, 430, 61, 25))
        self.lineEdit_28.setObjectName("lineEdit_28")

        self.retranslateUi(trayectoria2)
        self.pushButton.clicked.connect(self.planeo)
        self.pushButton_15.clicked.connect(self.set1)
        self.pushButton_16.clicked.connect(self.set2)
        self.lineEdit.editingFinished.connect(self.P1J1)
        self.lineEdit_2.editingFinished.connect(self.P1J2)
        self.lineEdit_3.editingFinished.connect(self.P1J3)
        self.lineEdit_8.editingFinished.connect(self.P1J4)
        self.lineEdit_9.editingFinished.connect(self.P1J5)
        self.lineEdit_7.editingFinished.connect(self.P1J6)
        self.lineEdit_6.editingFinished.connect(self.P2J1)
        self.lineEdit_4.editingFinished.connect(self.P2J2)
        self.lineEdit_5.editingFinished.connect(self.P2J3)
        self.lineEdit_10.editingFinished.connect(self.P2J4)
        self.lineEdit_11.editingFinished.connect(self.P2J5)
        self.lineEdit_12.editingFinished.connect(self.P2J6)
        self.lineEdit_14.editingFinished.connect(self.P3J1)
        self.lineEdit_13.editingFinished.connect(self.P3J2)
        self.lineEdit_17.editingFinished.connect(self.P3J3)
        self.lineEdit_16.editingFinished.connect(self.P3J4)
        self.lineEdit_18.editingFinished.connect(self.P3J5)
        self.lineEdit_15.editingFinished.connect(self.P3J6)
        self.lineEdit_19.editingFinished.connect(self.Repeticion)
        self.lineEdit_21.editingFinished.connect(self.P4J1)
        self.lineEdit_22.editingFinished.connect(self.P4J2)
        self.lineEdit_24.editingFinished.connect(self.P4J3)
        self.lineEdit_20.editingFinished.connect(self.P4J4)
        self.lineEdit_25.editingFinished.connect(self.P4J5)
        self.lineEdit_23.editingFinished.connect(self.P4J6)
        self.pushButton_18.clicked.connect(self.set4)
        self.pushButton_17.clicked.connect(self.set3)
        self.lineEdit_27.editingFinished.connect(self.velocidad)
        self.lineEdit_26.editingFinished.connect(self.aceleracion)
        self.lineEdit_28.editingFinished.connect(self.time)
        QtCore.QMetaObject.connectSlotsByName(trayectoria2)

    def retranslateUi(self, trayectoria2):
        _translate = QtCore.QCoreApplication.translate
        trayectoria2.setWindowTitle(_translate("trayectoria2", "Form"))
        self.pushButton.setText(_translate("trayectoria2", "Planear"))
        self.label_3.setText(_translate("trayectoria2", "J3"))
        self.label.setText(_translate("trayectoria2", "J1"))
        self.label_2.setText(_translate("trayectoria2", "J2"))
        self.label_6.setText(_translate("trayectoria2", "J6"))
        self.label_4.setText(_translate("trayectoria2", "J4"))
        self.label_5.setText(_translate("trayectoria2", "J5"))
        self.label_13.setText(_translate("trayectoria2", "Point1:"))
        self.pushButton_15.setText(_translate("trayectoria2", "SET"))
        self.label_7.setText(_translate("trayectoria2", "J5"))
        self.label_14.setText(_translate("trayectoria2", "Point2:"))
        self.label_8.setText(_translate("trayectoria2", "J4"))
        self.pushButton_16.setText(_translate("trayectoria2", "SET"))
        self.label_9.setText(_translate("trayectoria2", "J6"))
        self.label_10.setText(_translate("trayectoria2", "J2"))
        self.label_11.setText(_translate("trayectoria2", "J1"))
        self.label_12.setText(_translate("trayectoria2", "J3"))
        self.label_15.setText(_translate("trayectoria2", "J4"))
        self.label_16.setText(_translate("trayectoria2", "J2"))
        self.label_17.setText(_translate("trayectoria2", "J1"))
        self.label_18.setText(_translate("trayectoria2", "Point3:"))
        self.label_19.setText(_translate("trayectoria2", "J5"))
        self.label_20.setText(_translate("trayectoria2", "J6"))
        self.label_21.setText(_translate("trayectoria2", "J3"))
        self.pushButton_17.setText(_translate("trayectoria2", "SET"))
        self.label_22.setText(_translate("trayectoria2", "Cantidad de repeticiones:"))
        self.pushButton_18.setText(_translate("trayectoria2", "SET"))
        self.label_23.setText(_translate("trayectoria2", "J3"))
        self.label_24.setText(_translate("trayectoria2", "J2"))
        self.label_25.setText(_translate("trayectoria2", "J5"))
        self.label_26.setText(_translate("trayectoria2", "J1"))
        self.label_27.setText(_translate("trayectoria2", "J4"))
        self.label_28.setText(_translate("trayectoria2", "J6"))
        self.label_29.setText(_translate("trayectoria2", "Point4:"))
        self.pushButton_19.setText(_translate("trayectoria2", "Guardar"))
        self.label_30.setText(_translate("trayectoria2", "Aceleracion:"))
        self.label_31.setText(_translate("trayectoria2", "Velocidad:"))
        self.label_32.setText(_translate("trayectoria2", "(0-100%)"))
        self.label_33.setText(_translate("trayectoria2", "Tiempo de planeacion:"))
        self.label_34.setText(_translate("trayectoria2", "s"))
        self.label_35.setText(_translate("trayectoria2", "(0-100%)"))

        self.lineEdit_19.setText("1")
        self.repetir=int(self.lineEdit_19.text())
        
        self.M11=M11
        self.M21=M21
        self.M31=M31
        self.M41=M41
        self.M51=M51
        self.M61=M61
        self.M12=M12
        self.M22=M22
        self.M32=M32
        self.M42=M42
        self.M52=M52
        self.M62=M62
        self.M13=M13
        self.M23=M23
        self.M33=M33
        self.M43=M43
        self.M53=M53
        self.M63=M63
        self.M14=M14
        self.M24=M24
        self.M34=M34
        self.M44=M44
        self.M54=M54
        self.M64=M64

        self.iM11=int(self.M11*68)    #  // radians
        self.iM21=int(self.M21*65)      #  // radians-0.6   1.37
        self.iM31=int(self.M31*57.6)    #  // radians 0 2.5
        self.iM41=int(self.M11*61.11)  #  // radians -2.7 
        self.iM51=int(self.M21*57.78)  
        self.iM61=int(self.M31*64.35) 
        self.iM12=int(self.M12*68)    #  // radians
        self.iM22=int(self.M22*65)      #  // radians-0.6   1.37
        self.iM32=int(self.M32*57.6)    #  // radians 0 2.5
        self.iM42=int(self.M42*61.11)  #  // radians -2.7 
        self.iM52=int(self.M52*57.78)  
        self.iM62=int(self.M62*64.35) 
        self.iM13=int(self.M13*68)    #  // radians
        self.iM23=int(self.M23*65)      #  // radians-0.6   1.37
        self.iM33=int(self.M33*57.6)    #  // radians 0 2.5
        self.iM43=int(self.M43*61.11)  #  // radians -2.7 
        self.iM53=int(self.M53*57.78)  
        self.iM63=int(self.M63*64.35) 
        self.iM14=int(self.M14*68)    #  // radians
        self.iM24=int(self.M24*65)      #  // radians-0.6   1.37
        self.iM34=int(self.M34*57.6)    #  // radians 0 2.5
        self.iM44=int(self.M44*61.11)  #  // radians -2.7 
        self.iM54=int(self.M54*57.78)  
        self.iM64=int(self.M64*64.35) 

        self.lineEdit.setText(str(self.iM11))
        self.lineEdit_2.setText(str(self.iM21))
        self.lineEdit_3.setText(str(self.iM31))
        self.lineEdit_8.setText(str(self.iM41))
        self.lineEdit_9.setText(str(self.iM51))
        self.lineEdit_7.setText(str(self.iM61))
        self.lineEdit_6.setText(str(self.iM12))
        self.lineEdit_4.setText(str(self.iM22))
        self.lineEdit_5.setText(str(self.iM32))
        self.lineEdit_10.setText(str(self.iM42))
        self.lineEdit_11.setText(str(self.iM52))
        self.lineEdit_12.setText(str(self.iM62))
        self.lineEdit_14.setText(str(self.iM13))
        self.lineEdit_13.setText(str(self.iM23))
        self.lineEdit_17.setText(str(self.iM33))
        self.lineEdit_16.setText(str(self.iM43))
        self.lineEdit_18.setText(str(self.iM53))
        self.lineEdit_15.setText(str(self.iM63))
        self.lineEdit_21.setText(str(self.iM14))
        self.lineEdit_22.setText(str(self.iM24))
        self.lineEdit_24.setText(str(self.iM34))
        self.lineEdit_20.setText(str(self.iM44))
        self.lineEdit_25.setText(str(self.iM54))
        self.lineEdit_23.setText(str(self.iM64))
        self.lineEdit_26.setText(str(10))
        self.lineEdit_27.setText(str(10))
        self.lineEdit_28.setText(str(0.5))
    
    def aceleracion(self):
         self.Aci= float(self.lineEdit_26.text())
         self.Ac= (self.Aci/100)

    def velocidad(self): 
         self.Vei= float(self.lineEdit_27.text())
         self.Ve= (self.Vei/100)

    def time(self):
         self.Tm= float(self.lineEdit_28.text())
             
    def planeo(self):

        while self.repetir!=0:
            
            self.M1=float(self.M11)   #  // radians
            self.M2=float(self.M21 )    #  // radians-0.6   1.37
            self.M3=float(self.M31)   #  // radians 0 2.5
            self.M4=float(self.M41)  #  // radians -2.7 
            self.M5=float(self.M51)
            self.M6=float(self.M61 )
            self.plano()

            self.M1=float(self.M12)   #  // radians
            self.M2=float(self.M22)    #  // radians-0.6   1.37
            self.M3=float(self.M32)   #  // radians 0 2.5
            self.M4=float(self.M42)  #  // radians -2.7 
            self.M5=float(self.M52)
            self.M6=float(self.M62) 
            self.plano()

            self.M1=float(self.M13)  #  // radians
            self.M2=float(self.M23)     #  // radians-0.6   1.37
            self.M3=float(self.M33)   #  // radians 0 2.5
            self.M4=float(self.M43)  #  // radians -2.7 
            self.M5=float(self.M53)
            self.M6=float(self.M63)
            self.plano()

            self.M1=float(self.M14)  #  // radians
            self.M2=float(self.M24)     #  // radians-0.6   1.37
            self.M3=float(self.M34)   #  // radians 0 2.5
            self.M4=float(self.M44)  #  // radians -2.7 
            self.M5=float(self.M54)
            self.M6=float(self.M64)
            self.plano()

            self.repetir-=1
        self.repetir=int(self.lineEdit_19.text())

    def set1(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M11=self.joint_goal[0]    #  // radians
        self.M21=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M31=self.joint_goal[2]   #  // radians 0 2.5
        self.M41=self.joint_goal[3]  #  // radians -2.7 
        self.M51=self.joint_goal[4] 
        self.M61=self.joint_goal[5] 

        self.iM11=int(self.joint_goal[0]*68)    #  // radians
        self.iM21=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM31=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
        self.iM41=int(self.joint_goal[3]*61.11)  #  // radians -2.7 
        self.iM51=int(self.joint_goal[4]*57.78)  
        self.iM61=int(self.joint_goal[5]*64.35) 
    
        self.lineEdit.setText(str(self.iM11))
        self.lineEdit_2.setText(str(self.iM21 ))
        self.lineEdit_3.setText(str(self.iM31 ))
        self.lineEdit_8.setText(str(self.iM41 ))
        self.lineEdit_9.setText(str(self.iM51))
        self.lineEdit_7.setText(str(self.iM61 ))
    
        

    def Repeticion(self):
        self.repetir=int(self.lineEdit_19.text())
        print("Repetir")
        self.printear()

    def set2(self):
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M12=self.joint_goal[0]    #  // radians
        self.M22=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M32=self.joint_goal[2]   #  // radians 0 2.5
        self.M42=self.joint_goal[3]  #  // radians -2.7 
        self.M52=self.joint_goal[4] 
        self.M62=self.joint_goal[5] 

        self.iM12=int(self.joint_goal[0]*68)    #  // radians
        self.iM22=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM32=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
        self.iM42=int(self.joint_goal[3]*61.11)  #  // radians -2.7 
        self.iM52=int(self.joint_goal[4]*57.78)  
        self.iM62=int(self.joint_goal[5]*64.35) 
    
        self.lineEdit_6.setText(str(self.iM12))
        self.lineEdit_4.setText(str(self.iM22 ))
        self.lineEdit_5.setText(str(self.iM32 ))
        self.lineEdit_10.setText(str(self.iM42 ))
        self.lineEdit_11.setText(str(self.iM52))
        self.lineEdit_12.setText(str(self.iM62 ))
        print ("set2")
    
    def set3(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M13=self.joint_goal[0]    #  // radians
        self.M23=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M33=self.joint_goal[2]   #  // radians 0 2.5
        self.M43=self.joint_goal[3]  #  // radians -2.7 
        self.M53=self.joint_goal[4] 
        self.M63=self.joint_goal[5] 

        self.iM13=int(self.joint_goal[0]*68)    #  // radians
        self.iM23=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM33=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
        self.iM43=int(self.joint_goal[3]*61.11)  #  // radians -2.7 
        self.iM53=int(self.joint_goal[4]*57.78)  
        self.iM63=int(self.joint_goal[5]*64.35) 
    
        self.lineEdit_14.setText(str(self.iM13))
        self.lineEdit_13.setText(str(self.iM23 ))
        self.lineEdit_17.setText(str(self.iM33 ))
        self.lineEdit_16.setText(str(self.iM43 ))
        self.lineEdit_18.setText(str(self.iM53))
        self.lineEdit_15.setText(str(self.iM63 ))
        print ("Set3")
        
    def set4(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M14=self.joint_goal[0]    #  // radians
        self.M24=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M34=self.joint_goal[2]   #  // radians 0 2.5
        self.M44=self.joint_goal[3]  #  // radians -2.7 
        self.M54=self.joint_goal[4] 
        self.M64=self.joint_goal[5] 

        self.iM14=int(self.joint_goal[0]*68)    #  // radians
        self.iM24=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM34=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
        self.iM44=int(self.joint_goal[3]*61.11)  #  // radians -2.7 
        self.iM54=int(self.joint_goal[4]*57.78)  
        self.iM64=int(self.joint_goal[5]*64.35) 
    
        self.lineEdit_21.setText(str(self.iM14))
        self.lineEdit_22.setText(str(self.iM24 ))
        self.lineEdit_24.setText(str(self.iM34 ))
        self.lineEdit_20.setText(str(self.iM44 ))
        self.lineEdit_25.setText(str(self.iM54))
        self.lineEdit_23.setText(str(self.iM64 ))
        print ("Set4")
        

    def P1J1(self):
        self.iM11=int(self.lineEdit.text())
        self.M11=float(self.iM11)/68
        print(self.M11)
    
    def P1J2(self):
        self.iM21=int(self.lineEdit_2.text())
        self.M21=float(self.iM12)/65
        print(self.M21)

    def P1J3(self):
        self.iM31=int(self.lineEdit_3.text())
        self.M31=float(self.iM31)/57.6
        print(self.M31)
    
    def P1J4(self):
        self.iM41=int(self.lineEdit_8.text())
        self.M41=float(self.iM41)/61.11
        print(self.M41)

    def P1J5(self):
        self.iM51=int(self.lineEdit_7.text())
        self.M51=float(self.iM51)/57.78
        print(self.M51)  
    
    def P1J6(self):
        self.iM61=int(self.lineEdit_6.text())
        self.M61=float(self.iM61)/64.35
        print(self.M61)    
    
    def P2J1(self):
        self.iM12=int(self.lineEdit_4.text())
        self.M12=float(self.iM12)/68
        print(self.M12)    
    
    def P2J2(self):
        self.iM22=int(self.lineEdit_4.text())
        self.M22=float(self.iM22)/65
        print(self.M22)   

    def P2J3(self):
        self.iM32=int(self.lineEdit_5.text())
        self.M32=float(self.iM32)/57.6
        print(self.M32)   

    def P2J4(self):
        self.iM42=int(self.lineEdit_10.text())
        self.M42=float(self.iM42)/61.11
        print(self.M42)   

    def P2J5(self):
        self.iM52=int(self.lineEdit_11.text())
        self.M52=float(self.iM52)/57.78
        print(self.M52)    
    
    def P2J6(self):
        self.iM62=int(self.lineEdit_12.text())
        self.M62=float(self.iM62)/64.35
        print(self.M62)   
    
     
    def P3J1(self):
        self.iM13=int(self.lineEdit_14.text())
        self.M13=float(self.iM13)/68
        print(self.M13)   
    
    def P3J2(self):
        self.iM23=int(self.lineEdit_13.text())
        self.M23=float(self.iM23)/65
        print(self.M23)   

    def P3J3(self):
        self.iM33=int(self.lineEdit_17.text())
        self.M33=float(self.iM33)/57.6
        print(self.M33)   
    
    def P3J4(self):
        self.iM43=int(self.lineEdit_16.text())
        self.M43=float(self.iM43)/61.11
        print(self.M43)   

    def P3J5(self):
        self.iM53=int(self.lineEdit_18.text())
        self.M53=float(self.iM53)/57.78
        print(self.M53)    
    
    def P3J6(self):
        self.iM63=int(self.lineEdit_15.text())
        self.M63=float(self.iM63)/64.35
        print(self.M63)  

    def P4J1(self):
        self.iM14=int(self.lineEdit_21.text())
        self.M14=float(self.iM14)/68
        print(self.M14)   
    
    def P4J2(self):
        self.iM24=int(self.lineEdit_22.text())
        self.M24=float(self.iM24)/65
        print(self.M24)   

    def P4J3(self):
        self.iM34=int(self.lineEdit_24.text())
        self.M34=float(self.iM34)/57.6
        print(self.M34)   
    
    def P4J4(self):
        self.iM44=int(self.lineEdit_20.text())
        self.M44=float(self.iM44)/61.11
        print(self.M44)   

    def P4J5(self):
        self.iM54=int(self.lineEdit_25.text())
        self.M54=float(self.iM54)/57.78
        print(self.M54)    
    
    def P4J6(self):
        self.iM64=int(self.lineEdit_23.text())
        self.M64=float(self.iM64)/64.35
        print(self.M64)      
    
    def save(self):
         self.f=open("Trayectoria2.py", "w")
         self.f.write ("M11 =" + str(self.M11)+ "\n")
         self.f.write ("M21 =" + str(self.M21)+ "\n")
         self.f.write ("M31 =" + str(self.M31)+ "\n")
         self.f.write ("M41 =" + str(self.M41)+ "\n")
         self.f.write ("M51 =" + str(self.M51)+ "\n")
         self.f.write ("M61 =" + str(self.M61)+ "\n")

         self.f.write ("M12 =" +str(self.M12)+ "\n")
         self.f.write ("M22 =" +str(self.M22)+ "\n")
         self.f.write ("M32 =" +str(self.M32)+ "\n")
         self.f.write ("M42 =" +str(self.M42)+ "\n")
         self.f.write ("M52 =" +str(self.M52)+ "\n")
         self.f.write ("M62 =" +str(self.M62)+ "\n")

         self.f.write ("M13 =" +str(self.M13)+ "\n")
         self.f.write ("M23 =" +str(self.M23)+ "\n")
         self.f.write ("M33 =" +str(self.M33)+ "\n")
         self.f.write ("M43 =" +str(self.M43)+ "\n")
         self.f.write ("M53 =" +str(self.M53)+ "\n")
         self.f.write ("M63 =" +str(self.M63)+ "\n")
    
         self.f.write ("M14 =" +str(self.M14)+ "\n")
         self.f.write ("M24 =" +str(self.M24)+ "\n")
         self.f.write ("M34 =" +str(self.M34)+ "\n")
         self.f.write ("M44 =" +str(self.M44)+ "\n")
         self.f.write ("M54 =" +str(self.M54)+ "\n")
         self.f.write ("M64 =" +str(self.M64)+ "\n")
         self.f.close()

    def printear(self):
        
        print(self.M11)
        print(self.M21)
        print(self.M31)
        print(self.M41)
        print(self.M51)
        print(self.M61)
        
        print(self.M12)
        print(self.M22)
        print(self.M32)
        print(self.M42)
        print(self.M52)
        print(self.M62)

        print(self.M13)
        print(self.M23)
        print(self.M33)
        print(self.M43)
        print(self.M53)
        print(self.M63)

        print(self.M14)
        print(self.M24)
        print(self.M34)
        print(self.M44)
        print(self.M54)
        print(self.M64)


    def plano(self):
        
        print('Entre a la funcion planear')
        # We can get the joint values from the group and adjust some of the values:
        self.joint_goal = self.move_group.get_current_joint_values()
        print(self.joint_goal)

        # joint_goal[1] = 0
        # joint_goal[2] = 0
        # joint_goal[3] = 0
        # joint_goal[4] = 0
        # joint_goal[5] = 0
        # joint_goal[6] = 0
       
        #cambiar joint values
        self.joint_goal[0] = float(self.M1)    #  // radians
        self.joint_goal[1] = float(self.M2)   #  // radians-0.6   1.37
        self.joint_goal[2] = float(self.M3)  #  // radians 0 2.5
        self.joint_goal[3] = float(self.M4) #  // radians -2.7 
        self.joint_goal[4] = float(self.M5)#  // radians 1.8
        self.joint_goal[5] = float(self.M6)#  // radians 2.3
        
       
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        self.move_group.set_max_acceleration_scaling_factor(self.Ac)
        self.move_group.set_max_velocity_scaling_factor(self.Ve)
        self.move_group.set_joint_value_target(self.joint_goal)
        self.plan = self.move_group.go( wait=True)
        #plan = move_group.go(joint_goal, wait=True)
        print("after planning")
        # Calling ``stop()`` ensures that there is no residual movement
        self.move_group.stop()
        #joint_goal[0] =1.57  #;  // radians
        #joint_goal[1] = 0.0 #;  // radians
        #joint_goal[2] = 0.0 #;  // radians
        #joint_goal[3] = 0.0 #  // radians
        #joint_goal[4] = 0.0 #;  // radians
        #joint_goal[5] = 0.0 #;  // radians
        #move_group.execute(plan,  wait=True)
        #move_group.set_joint_value_target(joint_goal)
        # plan = move_group.go( wait=True)
        rospy.sleep(self.Tm)                                                 
        print("end")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trayectoria2 = QtWidgets.QWidget()
    ui = Ui_trayectoria2()
    ui.setupUi(trayectoria2)
    trayectoria2.show()
    sys.exit(app.exec_())
