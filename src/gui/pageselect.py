from gui.windows.loginWindow import LoginWindow
from gui.windows.landingWindow import LandingWindow
from gui.windows.registerWindow import RegisterWindow
from PyQt6.QtWidgets import (QMainWindow,QStackedWidget)

class PageSelect(QMainWindow):    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        #initiation of Windows
        self.setWindowTitle('Library')
        self.loginWindow = LoginWindow(self)
        self.registerWindow = RegisterWindow(self)
        self.landingWindow = LandingWindow(self)
        
        #Add them to ustom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.registerWindow)
        self.pages.addWidget(self.landingWindow)

        #Display the Loginpage as default
        self.pages.setCurrentIndex(0)
        self.pages.show()
        
        #Signals from Children
        self.loginWindow.sendUser.connect(self.setUser)
        #Signal from RegistrationBtn
        self.loginWindow.pageSwap.connect(self.registrationPage)
        #Signal from LoginBtn
        self.registerWindow.pageSwap.connect(self.loginPage)
    
    def registrationPage(self, text):
        print('Registration Window '+ text)
        self.changeStackedWidget(1)

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeStackedWidget(0)

    def setUser(self, user):
        self.userId = user
        print('main window got signal')
        self.changeStackedWidget(2)
        self.landingWindow.setUserid(self.userId)

        
    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)