from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import os





class MainWindow(QMainWindow):
    '''Class to construct app main window graphics'''


    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.setFixedSize(500,500)





    def SetUp(self):
        self.button=QPushButton(self)
        self.button.setText('Browse Files')
        self.button.setFixedSize(150,30)
        self.button.move(175,150)
        self.button.clicked.connect(self.browseFiles)
        self.run_button=QPushButton(self)
        self.run_button.setEnabled(False)
        self.run_button.setText('Run')
        self.run_button.move(200,200)
        self.path=QLabel(self)
        self.path.setFixedSize(450,100)
        self.path.move(100,200)
        self.path.adjustSize()




    def browseFiles(self):
        self.folderpath= QtWidgets.QFileDialog.getExistingDirectory(self)
        print(self.folderpath)
        if len(self.folderpath[0]) > 0:
            self.path.setText('Selected Folder:'+self.folderpath)
            self.run_button.setEnabled(True)








if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyle('Fusion')
    window=MainWindow()
    window.SetUp()
    window.show()
    sys.exit(app.exec())