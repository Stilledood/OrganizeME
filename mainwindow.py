from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
import os
from functions import run






class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(500,500)



    def browse_files(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        if len(self.folderpath) > 0:
            self.run_button.setEnabled(True)
            self.path.setText('Selected Folder:'+self.folderpath)





    def SetupUi(self):
        vbox=QVBoxLayout()
        self.button=QPushButton(self)
        self.button.setText('Browse files')
        self.button.setFixedSize(150,30)
        self.button.move(175,200)
        vbox.addWidget(self.button)





        self.button.clicked.connect(self.browse_files)




        self.sub_window=Options_window()
        self.run_button=QPushButton(self)
        self.run_button.setEnabled(False)
        self.run_button.setText("Run")
        self.run_button.move(200,250)
        self.path = QLabel(self)
        self.path.setFixedSize(400,50)
        self.path.move(50,400)
        self.path.adjustSize()

        vbox.addWidget(self.run_button)
        vbox.addWidget(self.path)
        self.setLayout(vbox)



        self.run_button.clicked.connect(self.sub_window.show)
        self.sub_window.save_button.clicked.connect(self.run_settings)

    def run_settings(self):
        files_type=self.sub_window.get_files_type()
        run(path=(r''+self.folderpath),typ_files=files_type)
        self.sub_window.save_button.setEnabled(True)







class Options_window(QWidget):
    def __init__(self):
        super(Options_window,self).__init__()
        self.resize(500,500)




        self.pictures_box = QCheckBox(self)
        self.pictures_box.setText('Pictures')
        self.pictures_box.move(100,150)

        self.video_box = QCheckBox(self)
        self.video_box.setText('Video')
        self.video_box.move(100, 200)

        self.music_box = QCheckBox(self)
        self.music_box.setText('Music')
        self.music_box.move(100, 250)

        self.pdf_box = QCheckBox(self)
        self.pdf_box.setText('PDF')
        self.pdf_box.move(100, 300)

        self.text_box = QCheckBox(self)
        self.text_box.setText('Text')
        self.text_box.move(100, 350)

        self.word_box = QCheckBox(self)
        self.word_box.setText('Word Files')
        self.word_box.move(100, 400)

        self.exe_box = QCheckBox(self)
        self.exe_box.setText('Executables')
        self.exe_box.move(100, 450)

        self.archives_box = QCheckBox(self)
        self.archives_box.setText('Archives')
        self.archives_box.move(100, 500)

        self.all_box = QCheckBox(self)
        self.all_box.setText('All Files')
        self.all_box.move(100, 550)



        box_resize=QGroupBox('Select what type of files you want to sort')
        resize_box=QVBoxLayout()
        resize_box.addWidget(self.pictures_box)
        resize_box.addWidget(self.video_box)
        resize_box.addWidget(self.music_box)
        resize_box.addWidget(self.pdf_box)
        resize_box.addWidget(self.text_box)
        resize_box.addWidget(self.word_box)
        resize_box.addWidget(self.archives_box)
        resize_box.addWidget(self.exe_box)
        resize_box.addWidget(self.all_box)



        box_resize.setLayout(resize_box)



        self.save_button = QPushButton(self)
        self.save_button.setText('OrGanizeME')
        self.save_button.setFixedSize(100, 30)
        self.save_button.move(200,200)
        save_button_box=QGroupBox("")
        save_button=QVBoxLayout()
        save_button.addWidget(self.save_button)
        save_button_box.setLayout(save_button)





        grid=QGridLayout()


        grid.addWidget(box_resize,0,1)
        grid.addWidget(save_button_box,1,1)
        self.setLayout(grid)
    def get_files_type(self):
        self.save_button.setEnabled(False)
        type_all_files = []
        if self.all_box.isChecked():
            type_all_files = ['Archives','Pictures','Video','PDF','Text','Music','Word Files','Executables']
            return type_all_files

        if self.archives_box.isChecked():
            type_all_files.append('Archives')
        if self.pictures_box.isChecked():
            type_all_files.append('Pictures')
        if self.video_box.isChecked():
            type_all_files.append('Video')
        if self.pdf_box.isChecked():
            type_all_files.append('PDF')
        if self.text_box.isChecked():
            type_all_files.append('Text')
        if self.music_box.isChecked():
            type_all_files.append('Music')
        if self.word_box.isChecked():
            type_all_files.append('Word Files')
        if self.exe_box.isChecked():
            type_all_files.append('Executables')
        print(type_all_files)

        return type_all_files










































if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle('Fusion')

    window=MainWindow()

    window.SetupUi()
    window.show()
    sys.exit(app.exec())