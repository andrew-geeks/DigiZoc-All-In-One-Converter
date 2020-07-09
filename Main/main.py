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
        self.setMaximumHeight(600)
        self.setMaximumWidth(900)
        self.setStyleSheet("background-color: white;")
        login_widget = Home(self)
        central_widget.addWidget(login_widget)
        
    def back_to_home(self):#back_function
        logged_in_widget = Home(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)

    def login(self):
        logged_in_widget = LoggedWidget(self)
        central_widget.addWidget(logged_in_widget)
        central_widget.setCurrentWidget(logged_in_widget)




class Home(QWidget): #Home_page
    def __init__(self,parent=None):
        super(Home, self).__init__(parent)
        welcome=QLabel('All In One Converter',self)
        welcome.move(7,7)
        welcome.setStyleSheet("QLabel {font: 25pt Times}")
        b1=QPushButton('Image\n Converters',self)
        b1.setStyleSheet("background-color:green; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b1.move(60,100)
        b2=QPushButton('Document\n Converters',self)
        b2.setStyleSheet("background-color:red; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b2.move(60,230)
        b3=QPushButton('Visual/Audio\n Converters',self)
        b3.setStyleSheet("background-color:black; font: bold 14px; min-width: 20em; min-height: 5em; border-radius: 10px;padding: 6px; color:white")
        b3.move(60,380)
        frame = QFrame(self)
        frame.resize(400,600)
        frame.move(500,0)
        frame.setStyleSheet("background-color: SlateBlue")
        #MainWindow.login(self)
    def image_page(self):
        pass
    def visual_page(self):
        pass
    def doc_page(self):
        pass




class LoginWidget(QWidget): #Anticipatory
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.button = QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        #self.button.clicked
        self.button.clicked.connect(self.parent().login)
        # you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
