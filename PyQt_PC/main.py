#! /usr/bin/python

import sys
import socket

#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
 
class demoBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(demoBoard, self).__init__()

        #set up the user interface from designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.getTemp.clicked.connect(self.getTemperature)
        self.ui.getPre.clicked.connect(self.getPressure)
        self.ui.displayText.clicked.connect(self.displayText)
        self.ui.setCfg.clicked.connect(self.setConfiguration)

    def setConfiguration(self):
        
        #Get ip address of the target
        self.ipAddr=self.ui.ipName.text()
        print self.ipAddr
        
        #int is needed for sock.sendto funtion
        self.portName=int(self.ui.portName.text())
        print self.portName
        
        #Choice between UDP and TCP
        mode=0
	if self.ui.checkBoxUDP.isChecked() == 1:
            mode = 0
        if self.ui.checkBoxTCP.isChecked() == 1:
            mode = 1
        print mode

        #TODO gestion des erreurs d'ouverture du port
        #TODO Implement TCP functionality
        self.sock=socket.socket(socket.AF_INET,    #internet
                                socket.SOCK_DGRAM) #UDP

    def getTemperature(self):
        self.sock.sendto("PRINT_TEMPERATURE", (self.ipAddr, self.portName))

        #TODO For further implementation
        self.ui.tempNum.setDigitCount(4)
	self.ui.tempNum.display("25.6")        

    def getPressure(self):
        self.sock.sendto("PRINT_PRESSURE", (self.ipAddr, self.portName))

        #TODO For further implementation
        self.ui.preNum.setDigitCount(7)
	self.ui.preNum.display("1024.14")

        #Send a message box to the user
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("PRINT_TEMP")

    def displayText(self):
        msg=self.ui.textToDisplay.text()
        cmd="PRINT_TEXT;"+msg

        #Display the received text on the rpi sense hat led matrix
        self.sock.sendto(cmd, (self.ipAddr, self.portName))
 
        #Send a debug message bo to the user
        QMessageBox.information(self,"Hello!","Current String is:\n"+msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sreen=demoBoard()
    sreen.show()
    sys.exit(app.exec_())