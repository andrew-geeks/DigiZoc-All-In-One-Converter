from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import img2pdf
from PIL import Image 
from fpdf import FPDF
from docx2pdf import convert
from moviepy.editor import *
import time

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
        heading=QLabel('Jpg to Png',self)
        heading.setStyleSheet("QLabel {font: 25pt Helvitica}")
        heading.move(360,0)
        self.bbutton=QPushButton(self)
        self.bbutton.setIcon(QIcon('main/files/backbutton.ico'))
        self.bbutton.setIconSize(QSize(30,30))
        self.bbutton.setFlat(True)
        self.bbutton.clicked.connect(lambda:MainWindow.back_to_home(self))
        self.bbutton.move(850,7)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('Main/files/logo.ico'))
    window = MainWindow()
    window.show()
    
    app.exec_()
