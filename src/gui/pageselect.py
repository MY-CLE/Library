from GUI.Windows.loginWindow import LoginWindow
from GUI.Windows.landingWindow import LandingWindow
from GUI.Windows.detailsWindow import DetailWindow
from PyQt6.QtWidgets import (QMainWindow, QStackedWidget)


class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.userId = None
        # initiation of Widows
        self.setWindowTitle('Liberary')
        self.loginWindow = LoginWindow(self)
        self.landingWindow = LandingWindow(self)
        #self.detailWindow = DetailWindow(self)

        # Add them to ustom Stacked Widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.loginWindow)
        self.pages.addWidget(self.landingWindow)
        # self.pages.addWidget(self.detailWindow)
        # Display the Loginpage as default
        self.pages.setCurrentIndex(1)
        self.pages.show()

        # Signals from Children
        # self.loginWindow.sendUser.connect(self.setUser)

    def setUser(self, user):
        self.userId = user
        print('main window got signal')
        self.changeStackedWidget(1)
        self.landingWindow.setUserid(self.userId)

    def changeStackedWidget(self, index):
        self.pages.setCurrentIndex(index)
