from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import img2pdf
from PIL import Image 
from fpdf import FPDF
from docx2pdf import convert
from moviepy.editor import *
import json
import threading

with open('path.json') as file:
    data=json.load(file)

a=data['main']
file_path=a['path']


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        global central_widget
        super(MainWindow, self).__init__(parent)
        central_widget = QStackedWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle('DigiZoc_v1.0')
        self.resize(900,600)
        
        #self.setMaximumHeight(600)
        #self.setMaximumWidth(900)
        self.setStyleSheet("background-color: white;")
        login_widget = Welcome(self)
        central_widget.addWidget(login_widget)
        
    def back_to_home(self):#back_function
        logged_in_widget = Home(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)

    def to_jpg_to_png(self):
        logged_in_widget = jpg_to_png(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)
    
    def to_settings_page(self):
        logged_in_widget = settings(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)

    def to_info_page(self):
        logged_in_widget = info_page(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)

class Home(QWidget): #Home_page
    def __init__(self,parent=None):
        global frame
        global framelayout
        super(Home, self).__init__(parent)
        welcome=QLabel('All In One Converter',self)
        welcome.move(7,7)
        welcome.setStyleSheet("QLabel {font: 25pt Times}")
        b1=QPushButton('Image\n Converters',self)
        b1.setStyleSheet("background-color:green; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b1.move(60,100)
        b1.clicked.connect(self.image_page)
        b2=QPushButton('Document\n Converters',self)
        b2.setStyleSheet("background-color:red; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b2.move(60,230)
        b2.clicked.connect(self.doc_page)
        b3=QPushButton('Visual/Audio\n Converters',self)
        b3.setStyleSheet("background-color:black; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b3.move(60,380)
        b3.clicked.connect(self.visual_page)
        frame=QFrame(self)
        frame.hide()
        framelayout=QVBoxLayout()
        settings=QPushButton(self)
        settings.setIcon(QIcon('main/files/settings.jpg'))
        settings.setIconSize(QSize(30,30))
        settings.setFlat(True)
        settings.move(0,560)
        settings.clicked.connect(lambda:MainWindow.to_settings_page(self))
    def image_page(self): 
        try:
            frame.show()
        except:
            pass
        try:
            for i in reversed(range(framelayout.count())): 
                framelayout.itemAt(i).widget().deleteLater()
        except:
            pass
        try:
            frame.setFixedSize(400,600)
            frame.move(500,0)
            frame.setStyleSheet("background-color: SlateBlue")
            frame.setLayout(framelayout)
        except:
            pass
        heading=QLabel('Image Converters')
        heading.setStyleSheet("QLabel {font: 25pt Times}")
        framelayout.addWidget(heading)
        b1=QPushButton('Jpg to Png')
        b1.setStyleSheet("background-color:green; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b1)
        b1.clicked.connect(lambda:MainWindow.to_jpg_to_png(self))
        b4=QPushButton('Jpg to pdf')
        b4.setStyleSheet("background-color:green; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b4)
        b5=QPushButton('Png to Ico')
        b5.setStyleSheet("background-color:green; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b5)
        
    def visual_page(self):
        try:
            frame.show()
        except:
            pass
        try:
             for i in reversed(range(framelayout.count())): 
                 framelayout.itemAt(i).widget().deleteLater()
        except:
            pass
        try:
            frame.setFixedSize(400,600)
            frame.move(500,0)
            frame.setStyleSheet("background-color: SlateBlue")
            frame.setLayout(framelayout)
        except:
            pass
        heading=QLabel('Visual/Audio Converters')
        heading.setStyleSheet("QLabel {font: 25pt Times}")
        framelayout.addWidget(heading)
        b1=QPushButton('Mp4 to Mp3')
        b1.setStyleSheet("background-color:black; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b1)

    
    def doc_page(self):
        try:
            frame.show()
        except:
            pass
        try:
            for i in reversed(range(framelayout.count())): 
                framelayout.itemAt(i).widget().deleteLater()
        except:
            pass
        try:
            frame.setFixedSize(400,600)
            frame.move(500,0)
            frame.setStyleSheet("background-color: SlateBlue")
            frame.setLayout(framelayout)
        except:
            pass
        heading=QLabel('Document Converters')
        heading.setStyleSheet("QLabel {font: 25pt Times}")
        framelayout.addWidget(heading)
        b1=QPushButton('Docx to Pdf')
        b1.setStyleSheet("background-color:red; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b1)
        b2=QPushButton('Txt to Pdf')
        b2.setStyleSheet("background-color:red; font: bold 14px; min-width: 7em; min-height: 2em; border-radius: 10px;padding: 6px; color:white")
        framelayout.addWidget(b2)




class Welcome(QWidget): #welcome_window_under_inspection
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.label_2=QLabel(self)
        self.label_2.move(80,40)
        self.label_2.setStyleSheet("background-image : url(Main/files/bg.jpg); background-attachment: fixed;")
        self.label_2.setText("") 
        self.label_2.resize(900,600)
        QTimer.singleShot(2000, lambda:MainWindow.back_to_home(self))


class jpg_to_png(QWidget): #jpg_to_png_page
    def __init__(self, parent=None):
        super(jpg_to_png, self).__init__(parent)
        self.label_2=QLabel(self)
        self.label_2.move(0,0)
        self.label_2.setStyleSheet("background-image : url(Main/files/b1.jpg); background-attachment: fixed;")
        self.label_2.setText("") 
        self.label_2.resize(900,600)
        heading=QLabel('Jpg to Png',self)
        #heading.setStyleSheet("QLabel {font: 25pt Helvitica}")
        heading.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        heading.setFont(QFont('Times',30))
        heading.move(360,10)
        self.bbutton=QPushButton(self)
        self.bbutton.setIcon(QIcon('main/files/backbutton.ico'))
        self.bbutton.setIconSize(QSize(30,30))
        self.bbutton.setFlat(True)
        self.bbutton.clicked.connect(lambda:MainWindow.back_to_home(self))
        self.bbutton.move(850,7)
        tlabel1=QLabel('*no file selected',self)
        tlabel1.move(100,250)
        self.line=QLabel('Select file to convert:',self)
        self.line.move(100,280)
        self.browse=QPushButton('Browse',self)
        self.browse.move(200,270)
        self.browse.clicked.connect(self.browse1)
    def browse1(self):
        fileName_=QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JPG (*.jpg);;All Files (*)")
        self.filenme=fileName_[0]
        fl=self.filenme.split('/')
        fname1=fl[len(fl)-1]
        f=fname1.split('.')
        self.fname=f[0]
        self.convert()
    def convert(self):
        try:
             Image.open(self.filenme).save(file_path+'/'+self.fname+'.png')
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setText("Conversion Complete")
             msg.setWindowTitle("Success")
             msg.setStandardButtons(QMessageBox.Ok)
             retval = msg.exec_()   
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Error)
            msg.setText("Conversion Failed")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()   

class path_change(QThread):#path_changing_class
    def __init__(self):
        QThread.__init__(self)
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C://',QFileDialog.ShowDirsOnly)
        if dir_=='':
            pass
        else:
            data={'main':{'path':dir_}}
            with open("path.json", "w") as write_file:
                json.dump(data, write_file)
            with open("path.json") as write_file:
                data=json.load(write_file)
                a=data['main']
                file_path=a['path']
            plabel.setText(file_path)   
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Output path changed!")
            msg.setWindowTitle("Done!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()       
    def __del__(self):
        self.wait()

    def run(self):
        # your logic here
        pass


class settings(QWidget): #settings_page
    def __init__(self, parent=None):
        super(settings,self).__init__(parent)
        global plabel
        self.label_2=QLabel(self)
        self.label_2.move(0,0)
        self.label_2.setStyleSheet("background-image : url(Main/files/b4.jpg); background-attachment: fixed;")
        self.label_2.setText("") 
        self.label_2.resize(900,600)
        heading=QLabel('Settings',self)
        #heading.setStyleSheet("QLabel {font: 25pt Helvitica}")
        heading.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        heading.setFont(QFont('Times',40))
        heading.move(370,10)
        self.bbutton=QPushButton(self)
        self.bbutton.setIcon(QIcon('main/files/backbutton.ico'))
        self.bbutton.setIconSize(QSize(30,30))
        self.bbutton.setFlat(True)
        self.bbutton.clicked.connect(lambda:MainWindow.back_to_home(self))
        self.bbutton.move(830,7)
        self.infob=QPushButton(self)
        self.infob.setIcon(QIcon('main/files/info.ico'))
        self.infob.setIconSize(QSize(40,40))
        self.infob.setFlat(True)
        self.infob.clicked.connect(lambda:MainWindow.to_info_page(self))
        self.infob.move(825,40)
        self.path=QLabel(self)
        plabel=QLabel('Output folder path: '+file_path,self)
        plabel.setWordWrap(True)
        plabel.setFont(QFont('Times',15))
        plabel.move(30,170)     
        
        self.change=QPushButton('Change',self)
        self.change.move(50,300)
        self.change.clicked.connect(self.thread_)
    def thread_(self):
        self.myThread = path_change()
        self.myThread.start()
    

class info_page(QWidget): #info_page
    def __init__(self, parent=None):
        super(info_page,self).__init__(parent)

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('Main/files/logo.ico'))
    window = MainWindow()
    window.show()
    
    app.exec_()
