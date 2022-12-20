from gui.windows.bookDetailsWindow import BookDetailsWindow
from gui.windows.landingWindow import LandingWindow
from gui.windows.loginWindow import LoginWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget, QFrame)

from gui.windows.registerWindow import RegisterWindow
from functional.book import Book
from gui.windows.userDetailsWindow import UserDetailsWindow
class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        # initiation of the Windows
        self.setWindowTitle('Library')
        self.loginWindow = LoginWindow(self)#0
        self.registerWindow = RegisterWindow(self)#1
        self.landingWindow = LandingWindow(self)#2
        self.userDetailsWindow = UserDetailsWindow(self)#3

        # Add them to custom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.registerWindow)
        self.pages.addWidget(self.landingWindow)
        self.pages.addWidget(self.userDetailsWindow)
        self.setCentralWidget(self.pages)
        # self.pages.addWidget(self.bookDetailsWindow)

        # Display the Loginpage as default
        self.pages.setCurrentIndex(0)
        #self.pages.show()

        # Signals from children
        self.loginWindow.sendUser.connect(self.setUser)
        # Signal from registrationForwardBtn
        self.loginWindow.pageSwap.connect(self.registrationPage)
        # Signal from loginBtn
        self.registerWindow.pageSwap.connect(self.loginPage)
        # Signal from registerBtn
        self.registerWindow.newUser.connect(self.newUser)
        # Signal from profilBtn
        self.landingWindow.UserEmail.connect(self.setUserProfilePage)
        # Singal for Book clicked
        self.landingWindow.bookView.bookclickedBookView.connect(
            self.bookclicked)
        # Signals for home button clicked
        self.landingWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.userDetailsWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        #Signals for logoutbtn clicked
        self.landingWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.userDetailsWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        #Signal for User Profile Page
        self.landingWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)


        #Signal for filling user Profile Page
        #self.userDetailsWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)


    def registrationPage(self, text):
        print('Registration Window ' + text)
        self.changeStackedWidget(1)

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeStackedWidget(0)

    def setUserProfilePage(self, email: str):
        self.userDetailsWindow.setUser(email)

    def userProfilePage(self):
        print('User Profile Window')
        self.changeStackedWidget(3)

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

    def bookclicked(self, book: Book):
        self.detailWindow = BookDetailsWindow(book)#4
        self.pages.addWidget(self.detailWindow)
        self.detailWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.detailWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.detailWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.changeStackedWidget(4)

    def returnHome(self):
        self.changeStackedWidget(2)

    def logout(self):
        self.changeStackedWidget(0)
        self.landingWindow.userid = None
