from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import os





class MainWindow(QMainWindow):
    '''Class to construct app main window graphics'''


    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(500,500)


    def SetUp(self):
        self.button=QPushButton(self)
        self.button.setText('Browse Files')
        self.button.setFixedSize(150,30)
        self.button.move(175,400)


    def resizeEvent(self,event):
        self.button.move(self.rect().center()-self.button.rect().center())
        QMainWindow.resizeEvent(self,event)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyle('Fusion')
    window=MainWindow()
    window.SetUp()
    window.show()
    sys.exit(app.exec())