from gui.windows.bookDetailsWindow import BookDetailsWindow
from gui.windows.landingWindow import LandingWindow
from gui.windows.loginWindow import LoginWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget)

from gui.windows.registerWindow import RegisterWindow
from gui.windows.userDetailsWindow import UserDetailsWindow
class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        # initiation of the Windows
        self.setWindowTitle('Library')
        self.loginWindow = LoginWindow(self)
        self.registerWindow = RegisterWindow(self)
        self.landingWindow = LandingWindow(self)
        self.bookDetailsWindow = BookDetailsWindow(self)
        self.userDetailsWindow = UserDetailsWindow(self)

        # Add them to custom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.registerWindow)
        self.pages.addWidget(self.landingWindow)
        self.pages.addWidget(self.bookDetailsWindow)
        self.pages.addWidget(self.userDetailsWindow)

        #Display the Loginpage as default
        self.pages.setCurrentIndex(4)
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
        self.landingWindow.bookView.bookclickedBookView.connect(self.bookclicked)
        #Signals for home button clicked
        self.landingWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.bookDetailsWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.userDetailsWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        #Signals for logoutbtn clicked
        self.landingWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.bookDetailsWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.userDetailsWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        #Signal for User Profile Page
        self.landingWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.bookDetailsWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.userDetailsWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)


    def registrationPage(self, text):
        print('Registration Window '+ text)
        self.changeStackedWidget(1)

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeStackedWidget(0)

    def userProfilePage(self, text):
        print('User Profile Window')
        self.changeStackedWidget(4)

    def setUser(self, userid):
        self.user = userid
        print('main window got signal')
        self.changeStackedWidget(2)
        self.landingWindow.setUserid(self.user.get_email())

    def newUser(self, user):
        print(f"INSERT VALUES{user.password}")
        print('New User in landingWindow')
        self.landingWindow.setUserid(user.email)
        self.changeStackedWidget(2)
        
    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)
    
    def bookclicked(self, index):
        self.changeStackedWidget(3)
    def returnHome(self):
        self.changeStackedWidget(2)
    
    def logout(self):   
        self.changeStackedWidget(0)
        self.landingWindow.userid = None

