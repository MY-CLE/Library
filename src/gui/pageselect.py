from gui.windows.loginWindow import LoginWindow
from gui.windows.landingWindow import LandingWindow
from PyQt6.QtWidgets import (QMainWindow,QStackedWidget)
class PageSelect(QMainWindow):    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        #initiation of Widows
        self.setWindowTitle('Liberary')
        self.loginWindow = LoginWindow(self)
        self.landingWindow = LandingWindow(self)
        
        #Add them to ustom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.landingWindow)
        #Display the Loginpage as default
        self.pages.setCurrentIndex(0)
        self.pages.show()
        
        #Signals from Children
        self.loginWindow.sendUser.connect(self.setUser)
    
    def setUser(self, user):
        self.userId = user
        print('main window got signal')
        self.changeStackedWidget(1)
        self.landingWindow.setUserid(self.userId)
        
    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)