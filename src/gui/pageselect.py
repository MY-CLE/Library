from gui.windows.landingWindow import LandingWindow

from gui.windows.detailsWindow import DetailWindow
from gui.windows.loginWindow import LoginWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget)

class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        # initiation of Widows
        self.setWindowTitle('Liberary')
        self.loginWindow = LoginWindow(self)
        self.registerWindow = RegisterWindow(self)
        self.landingWindow = LandingWindow(self)
        self.detailWindow = DetailWindow(self)

        # Add them to ustom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.registerWindow)
        self.pages.addWidget(self.landingWindow)
        self.pages.addWidget(self.detailWindow)

        #Display the Loginpage as default
        self.pages.setCurrentIndex(0)
        self.pages.show()
        
        #Signals from children
        self.loginWindow.sendUser.connect(self.setUser)
        #Signal from registrationForwardBtn
        self.loginWindow.pageSwap.connect(self.registrationPage)
        #Signal from loginBtn
        self.registerWindow.pageSwap.connect(self.loginPage)
        #Signal from registerBtn
        self.registerWindow.newUser.connect(self.newUser)
        #Singal for Book clicked
        self.landingWindow.libraryView.bookView.bookclickedBookView.connect(self.bookclicked)

    
    def registrationPage(self, text):
        print('Registration Window '+ text)
        self.changeStackedWidget(1)

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeStackedWidget(0)

    def setUser(self, user):
        self.user = user
        print('main window got signal')
        self.changeStackedWidget(2)
        self.landingWindow.setUserid(self.user.email())

    def newUser(self, user):
        print(f"INSERT VALUES{user.password}")
        print('New User in landingWindow')
        self.changeStackedWidget(2)
        
    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)
    
    def bookclicked(self, index):
        self.changeStackedWidget(3)
