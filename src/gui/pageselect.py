from GUI.windows.detailsWindow import DetailWindow
from GUI.windows.landingWindow import LandingWindow
from GUI.windows.loginWindow import LoginWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget)

from GUI.windows.registerWindow import RegisterWindow


class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        # initiation of Widows
        self.setWindowTitle('Liberary')
        self.loginWindow = LoginWindow(self)
        self.registerWindow = RegisterWindow(self)
        self.landingWindow = LandingWindow(self)
        #self.detailWindow = DetailWindow(self)

        # Add them to ustom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.registerWindow)
        self.pages.addWidget(self.landingWindow)
        # self.pages.addWidget(self.detailWindow)

        # Display the Loginpage as default
        self.pages.setCurrentIndex(2)
        self.pages.show()

        # Signals from children
        self.loginWindow.sendUser.connect(self.setUser)
        # Signal from registrationForwardBtn
        self.loginWindow.pageSwap.connect(self.registrationPage)
        # Signal from loginBtn
        self.registerWindow.pageSwap.connect(self.loginPage)
        # Signal from registerBtn
        self.registerWindow.newUser.connect(self.newUser)
        # Singal for Book clicked
        self.landingWindow.bookView.bookclickedBookView.connect(
            self.bookclicked)
        # Signals for home button clicked
        self.landingWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        # self.detailWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        # Signals for logoutbtn clicked

        self.landingWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        # self.detailWindow.sidebar.logoutBtn.clicked.connect(self.logout)

    def registrationPage(self, text):
        print('Registration Window ' + text)
        self.changeStackedWidget(1)

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeStackedWidget(0)

    def setUser(self, userid):
        self.userid = userid
        print('main window got signal')
        self.changeStackedWidget(2)
        self.landingWindow.setUserid(self.userid)

    def newUser(self, user):
        print(f"INSERT VALUES{user.password}")
        print('New User in landingWindow')
        self.landingWindow.setUserid(user.email)
        self.changeStackedWidget(2)

    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)

    def bookclicked(self, index):
        self.detailWindow = DetailWindow(index)
        self.pages.addWidget(self.detailWindow)
        self.detailWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.detailWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.changeStackedWidget(3)

    def returnHome(self):
        self.changeStackedWidget(2)

    def logout(self):
        self.changeStackedWidget(0)
        self.landingWindow.userid = None
