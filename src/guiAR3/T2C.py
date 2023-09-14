# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T2C.ui'
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
from Trayectoria2C import *

global M11,M21,M31
global M12,M22,M32
global M13,M23,M33
global M14,M24,M34

class Ui_T2C(object):
    def setupUi(self, T2C):
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

        self.M11=0.0
        self.M21=0.0
        self.M31=0.0
        
        self.M12=0.0
        self.M22=0.0
        self.M32=0.0
        
        self.M13=0.0
        self.M23=0.0
        self.M33=0.0
        
        self.M14=0.0
        self.M24=0.0
        self.M34=0.0

        self.Ac=0.1
        self.Ve=0.1
        self.Tm=5
        
        T2C.setObjectName("T2C")
        T2C.resize(424, 340)
        self.label_18 = QtWidgets.QLabel(T2C)
        self.label_18.setGeometry(QtCore.QRect(240, 50, 51, 17))
        self.label_18.setObjectName("label_18")
        self.label = QtWidgets.QLabel(T2C)
        self.label.setGeometry(QtCore.QRect(10, 70, 21, 20))
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(T2C)
        self.label_14.setGeometry(QtCore.QRect(130, 50, 51, 17))
        self.label_14.setObjectName("label_14")
        self.label_12 = QtWidgets.QLabel(T2C)
        self.label_12.setGeometry(QtCore.QRect(110, 150, 21, 20))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(T2C)
        self.label_11.setGeometry(QtCore.QRect(110, 70, 21, 20))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(T2C)
        self.label_13.setGeometry(QtCore.QRect(30, 50, 51, 17))
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(T2C)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 61, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 110, 61, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 70, 61, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(T2C)
        self.label_10.setGeometry(QtCore.QRect(110, 110, 21, 21))
        self.label_10.setObjectName("label_10")
        self.label_16 = QtWidgets.QLabel(T2C)
        self.label_16.setGeometry(QtCore.QRect(220, 110, 21, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_17.setGeometry(QtCore.QRect(240, 150, 61, 25))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 150, 61, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(T2C)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 21, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_13 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_13.setGeometry(QtCore.QRect(240, 110, 61, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 61, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(T2C)
        self.pushButton.setGeometry(QtCore.QRect(170, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 150, 61, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_17 = QtWidgets.QLabel(T2C)
        self.label_17.setGeometry(QtCore.QRect(220, 70, 21, 20))
        self.label_17.setObjectName("label_17")
        self.label_21 = QtWidgets.QLabel(T2C)
        self.label_21.setGeometry(QtCore.QRect(220, 150, 21, 20))
        self.label_21.setObjectName("label_21")
        self.lineEdit_14 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_14.setGeometry(QtCore.QRect(240, 70, 61, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_3 = QtWidgets.QLabel(T2C)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 21, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_18 = QtWidgets.QPushButton(T2C)
        self.pushButton_18.setGeometry(QtCore.QRect(320, 310, 81, 21))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_22 = QtWidgets.QLabel(T2C)
        self.label_22.setGeometry(QtCore.QRect(20, 220, 221, 17))
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_19.setGeometry(QtCore.QRect(230, 220, 61, 25))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_19 = QtWidgets.QLabel(T2C)
        self.label_19.setGeometry(QtCore.QRect(330, 70, 21, 20))
        self.label_19.setObjectName("label_19")
        self.lineEdit_15 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_15.setGeometry(QtCore.QRect(350, 110, 61, 25))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_16.setGeometry(QtCore.QRect(350, 70, 61, 25))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_23 = QtWidgets.QLabel(T2C)
        self.label_23.setGeometry(QtCore.QRect(330, 150, 21, 20))
        self.label_23.setObjectName("label_23")
        self.label_20 = QtWidgets.QLabel(T2C)
        self.label_20.setGeometry(QtCore.QRect(330, 110, 21, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_18 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_18.setGeometry(QtCore.QRect(350, 150, 61, 25))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_24 = QtWidgets.QLabel(T2C)
        self.label_24.setGeometry(QtCore.QRect(350, 50, 51, 17))
        self.label_24.setObjectName("label_24")
        self.pushButton_19 = QtWidgets.QPushButton(T2C)
        self.pushButton_19.setGeometry(QtCore.QRect(360, 180, 41, 21))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_15 = QtWidgets.QPushButton(T2C)
        self.pushButton_15.setGeometry(QtCore.QRect(40, 180, 41, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_17 = QtWidgets.QPushButton(T2C)
        self.pushButton_17.setGeometry(QtCore.QRect(250, 180, 41, 21))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_16 = QtWidgets.QPushButton(T2C)
        self.pushButton_16.setGeometry(QtCore.QRect(140, 180, 41, 21))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_25 = QtWidgets.QLabel(T2C)
        self.label_25.setGeometry(QtCore.QRect(20, 310, 191, 19))
        self.label_25.setObjectName("label_25")
        self.lineEdit_11 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 280, 61, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_26 = QtWidgets.QLabel(T2C)
        self.label_26.setGeometry(QtCore.QRect(210, 250, 79, 19))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(T2C)
        self.label_27.setGeometry(QtCore.QRect(210, 280, 79, 19))
        self.label_27.setObjectName("label_27")
        self.lineEdit_10 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 310, 61, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_28 = QtWidgets.QLabel(T2C)
        self.label_28.setGeometry(QtCore.QRect(20, 250, 111, 19))
        self.label_28.setObjectName("label_28")
        self.lineEdit_12 = QtWidgets.QLineEdit(T2C)
        self.lineEdit_12.setGeometry(QtCore.QRect(130, 250, 61, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_29 = QtWidgets.QLabel(T2C)
        self.label_29.setGeometry(QtCore.QRect(20, 280, 111, 19))
        self.label_29.setObjectName("label_29")

        self.retranslateUi(T2C)
        self.lineEdit.editingFinished.connect(self.P1J1)
        self.lineEdit_2.editingFinished.connect(self.P1J2)
        self.lineEdit_3.editingFinished.connect(self.P1J3)
        self.lineEdit_6.editingFinished.connect(self.P2J1)
        self.lineEdit_4.editingFinished.connect(self.P2J2)
        self.lineEdit_14.editingFinished.connect(self.P3J1)
        self.lineEdit_13.editingFinished.connect(self.P3J2)
        self.lineEdit_17.editingFinished.connect(self.P3J3)
        self.lineEdit_5.returnPressed.connect(self.P2J3)
        self.lineEdit_16.editingFinished.connect(self.P4J1)
        self.lineEdit_15.editingFinished.connect(self.P4J2)
        self.lineEdit_18.editingFinished.connect(self.P4J3)
        self.lineEdit_19.editingFinished.connect(self.REPETIR)
        self.pushButton.clicked.connect(self.PLANEAR)
        self.pushButton_18.clicked.connect(self.SAVE)
        self.pushButton_15.clicked.connect(self.set1)
        self.pushButton_16.clicked.connect(self.set2)
        self.pushButton_17.clicked.connect(self.set3)
        self.pushButton_19.clicked.connect(self.set4)
        self.lineEdit_12.editingFinished.connect(self.velocidad)
        self.lineEdit_11.editingFinished.connect(self.aceleracion)
        self.lineEdit_10.editingFinished.connect(self.time)
        QtCore.QMetaObject.connectSlotsByName(T2C)

    def retranslateUi(self, T2C):
        _translate = QtCore.QCoreApplication.translate
        T2C.setWindowTitle(_translate("T2C", "Form"))
        self.label_18.setText(_translate("T2C", "Point3:"))
        self.label.setText(_translate("T2C", "J1"))
        self.label_14.setText(_translate("T2C", "Point2:"))
        self.label_12.setText(_translate("T2C", "J3"))
        self.label_11.setText(_translate("T2C", "J1"))
        self.label_13.setText(_translate("T2C", "Point1:"))
        self.label_10.setText(_translate("T2C", "J2"))
        self.label_16.setText(_translate("T2C", "J2"))
        self.label_2.setText(_translate("T2C", "J2"))
        self.pushButton.setText(_translate("T2C", "Planear"))
        self.label_17.setText(_translate("T2C", "J1"))
        self.label_21.setText(_translate("T2C", "J3"))
        self.label_3.setText(_translate("T2C", "J3"))
        self.pushButton_18.setText(_translate("T2C", "Guardar"))
        self.label_22.setText(_translate("T2C", "Cantidad de repeticiones:"))
        self.label_19.setText(_translate("T2C", "J1"))
        self.label_23.setText(_translate("T2C", "J3"))
        self.label_20.setText(_translate("T2C", "J2"))
        self.label_24.setText(_translate("T2C", "Point4:"))
        self.pushButton_19.setText(_translate("T2C", "SET"))
        self.pushButton_15.setText(_translate("T2C", "SET"))
        self.pushButton_17.setText(_translate("T2C", "SET"))
        self.pushButton_16.setText(_translate("T2C", "SET"))
        self.label_25.setText(_translate("T2C", "Tiempo de planeacion:"))
        self.label_26.setText(_translate("T2C", "(0-100%)"))
        self.label_27.setText(_translate("T2C", "(0-100%)"))
        self.label_28.setText(_translate("T2C", "Velocidad:"))
        self.label_29.setText(_translate("T2C", "Aceleracion:"))

        self.lineEdit_19.setText("1")
        self.lineEdit_11.setText(str(10))
        self.lineEdit_12.setText(str(10))
        self.lineEdit_10.setText(str(5))
        self.repetir=int(self.lineEdit_19.text())
        
        self.M11=M11
        self.M21=M21
        self.M31=M31
        
        self.M12=M12
        self.M22=M22
        self.M32=M32
        
        self.M13=M13
        self.M23=M23
        self.M33=M33
        
        self.M14=M14
        self.M24=M24
        self.M34=M34
        

        self.iM11=int(self.M11*68)    #  // radians
        self.iM21=int(self.M21*65)      #  // radians-0.6   1.37
        self.iM31=int(self.M31*57.6)    #  // radians 0 2.5
        
        self.iM12=int(self.M12*68)    #  // radians
        self.iM22=int(self.M22*65)      #  // radians-0.6   1.37
        self.iM32=int(self.M32*57.6)    #  // radians 0 2.5
         
        self.iM13=int(self.M13*68)    #  // radians
        self.iM23=int(self.M23*65)      #  // radians-0.6   1.37
        self.iM33=int(self.M33*57.6)    #  // radians 0 2.5
         
        self.iM14=int(self.M14*68)    #  // radians
        self.iM24=int(self.M24*65)      #  // radians-0.6   1.37
        self.iM34=int(self.M34*57.6)    #  // radians 0 2.5

        self.lineEdit.setText(str(self.iM11))
        self.lineEdit_2.setText(str(self.iM21))
        self.lineEdit_3.setText(str(self.iM31))
        
        self.lineEdit_6.setText(str(self.iM12))
        self.lineEdit_4.setText(str(self.iM22))
        self.lineEdit_5.setText(str(self.iM32))
        
        self.lineEdit_14.setText(str(self.iM13))
        self.lineEdit_13.setText(str(self.iM23))
        self.lineEdit_17.setText(str(self.iM33))
       
        self.lineEdit_16.setText(str(self.iM14))
        self.lineEdit_15.setText(str(self.iM24))
        self.lineEdit_18.setText(str(self.iM34))

    def aceleracion(self):
         self.Aci= float(self.lineEdit_11.text())
         self.Ac= (self.Aci/100)
    def velocidad(self): 
         self.Vei= float(self.lineEdit_12.text())
         self.Ve= (self.Vei/100)
    def time(self):
         self.Tm= float(self.lineEdit_10.text())
    
    def PLANEAR(self):

        while self.repetir!=0:
            
            self.M1=float(self.M11)   #  // radians
            self.M2=float(self.M21 )    #  // radians-0.6   1.37
            self.M3=float(self.M31)   #  // radians 0 2.5
            self.plano()

            self.M1=float(self.M12)   #  // radians
            self.M2=float(self.M22)    #  // radians-0.6   1.37
            self.M3=float(self.M32)   #  // radians 0 2.5
            self.plano()

            self.M1=float(self.M13)  #  // radians
            self.M2=float(self.M23)     #  // radians-0.6   1.37
            self.M3=float(self.M33)   #  // radians 0 2.5
            self.plano()

            self.M1=float(self.M14)  #  // radians
            self.M2=float(self.M24)     #  // radians-0.6   1.37
            self.M3=float(self.M34)   #  // radians 0 2.5
            self.plano()

            self.repetir-=1
        self.repetir=int(self.lineEdit_19.text())

    def set1(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M11=self.joint_goal[0]    #  // radians
        self.M21=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M31=self.joint_goal[2]   #  // radians 0 2.5

        self.iM11=int(self.joint_goal[0]*68)    #  // radians
        self.iM21=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM31=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
    
        self.lineEdit.setText(str(self.iM11))
        self.lineEdit_2.setText(str(self.iM21 ))
        self.lineEdit_3.setText(str(self.iM31 ))

    def REPETIR(self):
        self.repetiri=int(self.lineEdit_19.text())
        if self.repetiri<=10:
            self.repetir=self.repetiri
            print("Repetir")
        if self.repetiri>10:
            self.repetir=1
            self.lineEdit_19.setText(str(1))
        self.printear()

    def set2(self):
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M12=self.joint_goal[0]    #  // radians
        self.M22=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M32=self.joint_goal[2]   #  // radians 0 2.5 

        self.iM12=int(self.joint_goal[0]*68)    #  // radians
        self.iM22=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM32=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5 
    
        self.lineEdit_6.setText(str(self.iM12))
        self.lineEdit_4.setText(str(self.iM22 ))
        self.lineEdit_5.setText(str(self.iM32 ))
        
        print ("set2")
    
    def set3(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M13=self.joint_goal[0]    #  // radians
        self.M23=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M33=self.joint_goal[2]   #  // radians 0 2.5 

        self.iM13=int(self.joint_goal[0]*68)    #  // radians
        self.iM23=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM33=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5 
    
        self.lineEdit_14.setText(str(self.iM13))
        self.lineEdit_13.setText(str(self.iM23 ))
        self.lineEdit_17.setText(str(self.iM33 ))
        
        print ("Set3")
        
    def set4(self):
        
        self.joint_goal = self.move_group.get_current_joint_values() 
        self.M14=self.joint_goal[0]    #  // radians
        self.M24=self.joint_goal[1]     #  // radians-0.6   1.37
        self.M34=self.joint_goal[2]   #  // radians 0 2.5

        self.iM14=int(self.joint_goal[0]*68)    #  // radians
        self.iM24=int(self.joint_goal[1]*65)      #  // radians-0.6   1.37
        self.iM34=int(self.joint_goal[2]*57.6)    #  // radians 0 2.5
    
        self.lineEdit_16.setText(str(self.iM14))
        self.lineEdit_15.setText(str(self.iM24 ))
        self.lineEdit_18.setText(str(self.iM34 ))

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
    
    def P4J1(self):
        self.iM14=int(self.lineEdit_16.text())
        self.M14=float(self.iM14)/68
        print(self.M14)   
    
    def P4J2(self):
        self.iM24=int(self.lineEdit_15.text())
        self.M24=float(self.iM24)/65
        print(self.M24)   

    def P4J3(self):
        self.iM34=int(self.lineEdit_18.text())
        self.M34=float(self.iM34)/57.6
        print(self.M34)   
    
    
    def SAVE(self):
         self.f=open("Trayectoria2C.py", "w")
         self.f.write ("M11 =" + str(self.M11)+ "\n")
         self.f.write ("M21 =" + str(self.M21)+ "\n")
         self.f.write ("M31 =" + str(self.M31)+ "\n")

         self.f.write ("M12 =" +str(self.M12)+ "\n")
         self.f.write ("M22 =" +str(self.M22)+ "\n")
         self.f.write ("M32 =" +str(self.M32)+ "\n")

         self.f.write ("M13 =" +str(self.M13)+ "\n")
         self.f.write ("M23 =" +str(self.M23)+ "\n")
         self.f.write ("M33 =" +str(self.M33)+ "\n")
    
         self.f.write ("M14 =" +str(self.M14)+ "\n")
         self.f.write ("M24 =" +str(self.M24)+ "\n")
         self.f.write ("M34 =" +str(self.M34)+ "\n")

         self.f.close()

    def printear(self):
        
        print(self.M11)
        print(self.M21)
        print(self.M31)
        
        print(self.M12)
        print(self.M22)
        print(self.M32)
        
        print(self.M13)
        print(self.M23)
        print(self.M33)

        print(self.M14)
        print(self.M24)
        print(self.M34)
  

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
        self.joint_goal = self.move_group.get_current_joint_values()
        if self.joint_goal[0]>=(self.M1+0.01) or self.joint_goal[0]<=(self.M1-0.01):
            print(self.M1)
            self.plano() 
            
        if self.joint_goal[1]>=self.M2+0.01 or self.joint_goal[1]<=self.M2-0.01:
           print(self.M2) 
           self.plano() 
            
        if self.joint_goal[2]>=self.M3+0.01 or self.joint_goal[2]<=self.M3-0.01:
           print(self.M3)
           self.plano()                                                                                  
        print("end")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    T2C = QtWidgets.QWidget()
    ui = Ui_T2C()
    ui.setupUi(T2C)
    T2C.show()
    sys.exit(app.exec_())