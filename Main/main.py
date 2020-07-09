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
        welcome=QLabel('Welcome,',self)
        welcome.move(3,7)
        welcome.setStyleSheet("QLabel {font: 30pt Times}")
        #MainWindow.login(self)





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
