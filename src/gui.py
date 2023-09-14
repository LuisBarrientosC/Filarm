# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Dec 30 18:46:24 2022
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

#-------------------------ROS IMPORTS----------------------------------

#-------------------------QT IMPORTS----------------------------------
from PySide import QtCore, QtGui

#-------------------------DECLARACIONES----------------------------------
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

#-------------------------_fromUtf8 CODE----------------------------------
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
#-------------------------qt CONFIG----------------------------------
class Ui_Form(object):
    def setupUi(self, Form):

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
        
        rospy.Subscriber("joy", Joy, self.control) 
        #rospy.Subscriber('position_state_x', Float32, callback)
        #rospy.Subscriber('position_state_y', Float32, callback1)
        
        #---------------------MOTORES---------------------------------
        self.M1=0.0
        self.M2=0.0
        self.M3=0.0
        self.M4=0.0
        self.M5=0.0
        self.M6=0.0
        #--------------------BOTONES---------------------------------
        self.xbox_status=0
        self.counter=0
        self.A=0.0   
        self.B=0.0  
        self.PyQt4X=0.0
        self.Y=0.0
        self.RB=0.0
        self.LB=0.0
        self.DI=0.0  #Boton derecha/izquierda
        self.UD=0.0  #Boton UP/DOWN
        self.SQ=0.0 
        #---------------------------------------------------------------

        Form.setObjectName("Form")
        Form.resize(845, 610)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 80, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 140, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 20, 161, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(570, 280, 21, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(570, 310, 21, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(570, 350, 21, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(570, 390, 21, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(570, 430, 21, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(570, 470, 21, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(570, 510, 21, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 200, 161, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 550, 141, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 20, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 80, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(760, 270, 61, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(760, 310, 61, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(760, 350, 61, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(760, 510, 61, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(760, 470, 61, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(760, 390, 61, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtGui.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(760, 430, 61, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(590, 280, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(-170)
        self.horizontalSlider.setMaximum(170)
        self.horizontalSlider_2 = QtGui.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(590, 310, 160, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(-40)
        self.horizontalSlider_2.setMaximum(90)
        self.horizontalSlider_3 = QtGui.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(590, 350, 160, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(144)
        self.horizontalSlider_4 = QtGui.QSlider(Form)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(590, 390, 160, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setMinimum(-165)
        self.horizontalSlider_4.setMaximum(165)
        self.horizontalSlider_5 = QtGui.QSlider(Form)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(590, 430, 160, 16))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_5.setMinimum(-104)
        self.horizontalSlider_5.setMaximum(104)
        self.horizontalSlider_6 = QtGui.QSlider(Form)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(590, 510, 160, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalSlider_6.setMinimum(-148)
        self.horizontalSlider_6.setMaximum(148)
        self.horizontalSlider_7 = QtGui.QSlider(Form)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(590, 470, 160, 16))
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.horizontalSlider_7.setMinimum(-170)
        self.horizontalSlider_7.setMaximum(170)

        self.lineEdit.setText(str(self.M1))
        self.lineEdit_2.setText(str(self.M2))
        self.lineEdit_3.setText(str(self.M3))
        self.lineEdit_8.setText(str(self.M4))
        self.lineEdit_9.setText(str(self.M5))
        self.lineEdit_7.setText(str(self.M6))
        #-------------------DECLARACIONES-------------------
        #---------------------------------------------------
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.foto)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.video)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.posicioninicio)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modomanual)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modoautomatico)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.xbox)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.planear)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ1)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ2)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ3)
        QtCore.QObject.connect(self.lineEdit_8, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ4)
        QtCore.QObject.connect(self.lineEdit_9, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ5)
        QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ6)
        QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8 ("textEdited(QString)")), self.valorJ7)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J1)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J2)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J3)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J4)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J5)
        QtCore.QObject.connect(self.horizontalSlider_7, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J6)
        QtCore.QObject.connect(self.horizontalSlider_6, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.J7)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Modo Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Modo Automatico", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Posicion de inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "J1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "J2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "J3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "J4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "J5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "J6", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "J7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "XBOX", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "PLANEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Foto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "VIdeo", None, QtGui.QApplication.UnicodeUTF8))

#-----------------------------------------BUTTONS AND SLIDERS--------------------------------------------------------
    def foto(self):
        print ("Foto")
        

    def video(self):
        print ("Video")

    def posicioninicio(self):

        self.M1=0
        self.M2=0
        self.M3=1.4
        self.M4=0
        self.M5=0
        self.M6=1.59
        
        self.plano()

        print ("Posicion de inicio")

    def modomanual(self):
        self.M1= (self.horizontalSlider.value())
        self.lineEdit.setText(str(self.M1))
        self.M2= (self.horizontalSlider_2.value())
        self.lineEdit_2.setText(str(self.M2))
        self.M3= (self.horizontalSlider_3.value())
        self.lineEdit_3.setText(str(self.M3))
        self.M4= (self.horizontalSlider_4.value())
        self.lineEdit_8.setText(str(self.M4))
        self.M5= (self.horizontalSlider_5.value())
        self.lineEdit_9.setText(str(self.M5))
        self.M6= (self.horizontalSlider_7.value())
        self.lineEdit_7.setText(str(self.M6))
        self.xbox_status=0
        print(self.M1)
        print(self.M2)
        print(self.M3)
        print(self.M4)
        print(self.M5)
        print(self.M6)
        print ("Modo manual_GUI")
    
    def xbox(self):
        self.M1= (self.horizontalSlider.value())
        self.lineEdit.setText(str(self.M1))
        self.M2= (self.horizontalSlider_2.value())
        self.lineEdit_2.setText(str(self.M2))
        self.M3= (self.horizontalSlider_3.value())
        self.lineEdit_3.setText(str(self.M3))
        self.M4= (self.horizontalSlider_4.value())
        self.lineEdit_8.setText(str(self.M4))
        self.M5= (self.horizontalSlider_5.value())
        self.lineEdit_9.setText(str(self.M5))
        self.M6= (self.horizontalSlider_7.value())
        self.lineEdit_7.setText(str(self.M6))
        self.xbox_status=1
        print(self.M1)
        print(self.M2)
        print(self.M3)
        print(self.M4)
        print(self.M5)
        print(self.M6)
        print ("MODO_MANUAL_XBOX")
    
    def modoautomatico(self):
        self.xbox_status=2
        print ("Modo automatico")

    def planear(self):
        self.plano()
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
        float (self.M1)
        self.M1= (self.horizontalSlider.value())
        self.lineEdit.setText(str(self.M1))

    def J2(self):
        float (self.M2)
        self.M2= (self.horizontalSlider_2.value())
        self.lineEdit_2.setText(str(self.M2))

    def J3(self):
        float (self.M3)
        self.M3= (self.horizontalSlider_3.value())
        self.lineEdit_3.setText(str(self.M3))

    def J4(self):
        float (self.M4)
        self.M4= (self.horizontalSlider_4.value())
        self.lineEdit_8.setText(str(self.M4))

    def J5(self):
        float (self.M5)
        self.M5= (self.horizontalSlider_5.value())
        self.lineEdit_9.setText(str(self.M5))

    def J6(self):
        float (self.M6)
        self.M6= (self.horizontalSlider_7.value())
        self.lineEdit_7.setText(str(self.M6))

    def J7(self):
        print("FUERA DE SERVICIO")
        print(self.xbox_status)
    #    float (self.M7)
    #    self.M7= (self.horizontalSlider_7.value())
    #    self.lineEdit_6.setText(str(self.M7))
    
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
        self.joint_goal[0] = float(self.M1)/68    #  // radians
        self.joint_goal[1] = float(self.M2)/65    #  // radians-0.6   1.37
        self.joint_goal[2] = float(self.M3)/57.6  #  // radians 0 2.5
        self.joint_goal[3] = float(self.M4)/61.11 #  // radians -2.7 
        self.joint_goal[4] = float(self.M5)/57.78 #  // radians 1.8
        self.joint_goal[5] = float(self.M6)/64.35 #  // radians 2.3
        
       
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
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
        rospy.sleep(1)                                                 
        print("end")
    
    def control(self,data):

        self.A=data.buttons[0]  #Obtencion de los datos de los botones del control xbox
        self.B=data.buttons[1]
        self.X=data.buttons[2]
        self.Y=data.buttons[3]
        self.RB=data.buttons[5]
        self.LB=data.buttons[4]
        self.UD=data.axes[7]
        self.DI=data.axes[6]
        self.SQ=data.buttons[6]
        print(self.xbox_status)

        if self.xbox_status==1:

            if self.A==1 and self.DI==1 and self.M1<=2.0*68:           #Condiciones de los botones del xbox para 
                self.M1+=0.2*68  #;  // radians   #establecer cuantos radianes se movera el robot. 
                self.lineEdit.setText(str(self.M1))
                self.horizontalSlider.setValue(self.M1)
                print(self.M1)
                print("xbox_Control")
                self.plano()
        
            if self.A==1 and self.DI==-1 :
                self.M1+=-0.2*68  #;  // radians
                self.lineEdit.setText(str(self.M1))
                self.horizontalSlider.setValue(self.M1)
                print("xbox_Control")
                self.plano()
            
            if self.B==1 and self.UD==1 :
                self.M2-=0.1*65  #;  // radians
                self.lineEdit_2.setText(str(self.M2))
                self.horizontalSlider_2.setValue(self.M2)
                print("xbox_Control")
                self.plano()

            if self.B==1 and self.UD==-1 :
                self.M2+=0.1*65  #;  // radians
                self.lineEdit_2.setText(str(self.M2))
                self.horizontalSlider_2.setValue(self.M2)
                print("xbox_Control")
                self.plano()

            if self.Y==1 and self.UD==1 and self.M3>=0.1 :
                self.M3-=0.1*57.6 #;  // radians
                self.lineEdit_3.setText(str(self.M3))
                self.horizontalSlider_3.setValue(self.M3)
                print("xbox_Control")
                self.plano()

            if self.Y==1 and self.UD==-1 :
                self.M3+=0.1*57.6  #;  // radians
                self.lineEdit_3.setText(str(self.M3))
                self.horizontalSlider_3.setValue(self.M3)
                print("xbox_Control")
                self.plano()
            
            if self.X==1 and self.DI==1 :
                self.M4+=0.1*61.11 #;  // radians
                self.lineEdit_8.setText(str(self.M4))
                self.horizontalSlider_4.setValue(self.M4)
                print("xbox_Control")
                self.plano()

            if self.X==1 and self.DI==-1 :
                self.M4+=-0.1*61.11  #;  // radians
                self.lineEdit_8.setText(str(self.M4))
                self.horizontalSlider_4.setValue(self.M4)
                print("xbox_Control")
                self.plano()

            if self.RB==1 and self.UD==1 :
                self.M5-=0.1*57.78  #;  // radians
                self.lineEdit_9.setText(str(self.M5))
                self.horizontalSlider_5.setValue(self.M5)
                print("xbox_Control")
                self.plano()

            if self.RB==1 and self.UD==-1 :
                self.M5+=0.1*57.78  #;  // radians
                self.lineEdit_9.setText(str(self.M5))
                self.horizontalSlider_5.setValue(self.M5)
                print("xbox_Control")
                self.plano()

            if self.LB==1 and self.DI==1 :
                M6+=0.3*64.35  #;  // radians
                self.lineEdit_7.setText(str(self.M6))
                self.horizontalSlider_7.setValue(self.M6)
                print("xbox_Control")
                self.plano()

            if self.LB==1 and self.DI==-1 :
                self.M6+=-0.3*64.35  #;  // radians
                self.lineEdit_7.setText(str(self.M6))
                self.horizontalSlider_7.setValue(self.M6)
                print("xbox_Control")
                self.plano()

            if self.SQ==1 and self.A==1:
                xbox_status=0
                print("MODO_GUI")

            if self.SQ==1 and self.B==1:
                xbox_status=1
                print("MODO_CONTROL_XBOX")
            
            if self.SQ==1 and self.Y==1:
                self.counter=0
                xbox_status=2
                print("MODO_AUTOMATICO") 
            
            if self.SQ==1 and self.X==1:
                self.counter=0
                xbox_status=3
                print(xbox_status) 
            
            if self.SQ==1 and self.RB==1:
                self.counter=0
                xbox_status=4
                print(xbox_status) 

            if self.SQ==1 and self.LB==1:
                self.counter=0
                xbox_status=5
                print(xbox_status) 
            #if move==1:
            # move=0
            # planear()

if __name__ == "__main__":
    
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('robot_plan', anonymous=True)
    rospy.loginfo("robot_plan")
    
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

