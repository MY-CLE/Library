from gui.windows.loginWindow import LoginWindow
from gui.windows.landingWindow import LandingWindow
from PyQt6.QtWidgets import (QMainWindow,QStackedWidget)
from PyQt6.QtCore import pyqtSignal

class PageSelect(QMainWindow):    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        #initiation of Widows
        self.setWindowTitle('Liberary')
        self.loginWindow = LoginWindow(self)
        self.landingWindow = LandingWindow(self)
        
        #Add them to ustom Stacked Widget
        self.widget = Pages()
        self.widget.addWidget(self.loginWindow)
        self.widget.addWidget(self.landingWindow)
        
        #self.widget.setStyleSheet('background-color: #be06ff')
        #Display the Loginpage as default
        self.widget.setCurrentIndex(0)
        self.widget.show()
        self.loginWindow.sendUser.connect(self.setUser)
    
    def setUser(self, user):
        self.userId = user
        print('main window got signal')
        self.changeStackedWidget(1)
        self.landingWindow.setUserid(self.userId)
        
    def changeStackedWidget(self, index):
        self.widget.setCurrentIndex(index)
        
        
#This Custom Stac0kedWidegt is basicly the same as a normal one.
#but it has a custom function which allows the Children of it to
#change the visble widget
class Pages(QStackedWidget):    
    def __init__(self):
        super(QStackedWidget, self).__init__()