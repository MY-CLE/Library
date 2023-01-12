from gui.windows.borrowedBooksWindow import BorrowedBooksWindow
from gui.windows.bookDetailsWindow import BookDetailsWindow
from gui.windows.landingWindow import LandingWindow
from gui.windows.loginWindow import LoginWindow
from gui.windows.registerWindow import RegisterWindow
from gui.windows.userDetailsWindow import UserDetailsWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget, QFrame)

from functional.book import Book
from functional.account import Account
class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('Library')
        self.routes = {}
        self.loginWindow = LoginWindow(self)
        self.loginWindow.sendUser.connect(self.setUser)
        self.loginWindow.pageSwap.connect(self.registrationPage)
        
        self.registerWindow = RegisterWindow(self)
        self.registerWindow.pageSwap.connect(self.loginPage)
        self.registerWindow.newUser.connect(self.setUser)
        # Add them to custom Stacked Widget
        self.pages = QStackedWidget()
        self.routes['LoginWindow'] = self.pages.addWidget(self.loginWindow)
        self.routes['RegisterWindow'] = self.pages.addWidget(self.registerWindow)
        self.setCentralWidget(self.pages)
        self.changeWindowTo('LoginWindow')

    def changeWindowTo(self, pageName: str):
        index = self.routes[pageName]
        self.pages.setCurrentIndex(index)

    def registrationPage(self, text):
        print('Registration Window ' + text)
        self.changeWindowTo('RegisterWindow')

    def loginPage(self, text):
        print('Login Window ' + text)
        self.changeWindowTo('LoginWindow')

    def userProfilePage(self):
        self.userDetailsWindow = UserDetailsWindow(self)
        self.routes['UserDetailsWindow'] = self.pages.addWidget(self.userDetailsWindow)
        self.userDetailsWindow.setUser(self.user)
        self.userDetailsWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.userDetailsWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.changeWindowTo('UserDetailsWindow')
        
    def initLandingpage(self):
        self.landingWindow = LandingWindow(self)
        self.landingWindow.UserEmail.connect(self.userProfilePage)
        self.landingWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.landingWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.landingWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.landingWindow.sidebar.addBookBtn.clicked.connect(self.borrowedBooksPage)
        self.routes['LandingWindow'] = self.pages.addWidget(self.landingWindow)
        self.landingWindow.bookView.bookclickedBookView.connect(self.bookclicked)
    
    def borrowedBooksPage(self):
        self.borrowedBooksWindow = BorrowedBooksWindow(self.user)
        self.borrowedBooksWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.borrowedBooksWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.borrowedBooksWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.borrowedBooksWindow.bookView.bookclickedBookView.connect(self.bookclicked)
        self.routes['BorrowedBooksWindow'] = self.pages.addWidget(self.borrowedBooksWindow)
        self.changeWindowTo('BorrowedBooksWindow')
        

    def setUser(self, user: Account):
        self.user = user
        print('main window got signal')
        if not 'LandingWindow' in self.routes:
            self.initLandingpage()
        self.landingWindow.setUser(self.user)
        self.changeWindowTo('LandingWindow')


    def bookclicked(self, book: Book):
        self.bookDetailsWindow = BookDetailsWindow(book, self.user)
        self.routes['BookDetailsWindow'] = self.pages.addWidget(self.bookDetailsWindow)
        self.bookDetailsWindow.sidebar.homeBtn.clicked.connect(self.returnHome)
        self.bookDetailsWindow.sidebar.logoutBtn.clicked.connect(self.logout)
        self.bookDetailsWindow.sidebar.profileBtn.clicked.connect(self.userProfilePage)
        self.bookDetailsWindow.sidebar.addBookBtn.clicked.connect(self.borrowedBooksPage)
        self.changeWindowTo('BookDetailsWindow')

    def returnHome(self):
        self.changeWindowTo('LandingWindow')
        if 'BookDetailsWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('BookDetailsWindow')))
        if 'UserDetailsWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('UserDetailsWindow')))
        if 'BorrowedBooksWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('BorrowedBooksWindow')))

    def logout(self):
        self.changeWindowTo('LoginWindow')
        if 'BookDetailsWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('BookDetailsWindow')))
        if 'UserDetailsWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('UserDetailsWindow')))
        if 'LandingWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('LandingWindow')))
        if 'BorrowedBooksWindow' in self.routes:
            self.pages.removeWidget(self.pages.widget(self.routes.pop('BorrowedBooksWindow')))
