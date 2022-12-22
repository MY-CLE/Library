from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize, pyqtSignal
from gui.elements.bookView import BookView
from gui.elements.header import Header
from gui.elements.generalSidebar import SideBar
from database.dbfunctions import fetchBookCount


class LandingWindow(QFrame):
    UserEmail = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        self.user= None
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("landingWindow")
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)

        self.header = Header()
        self.sidebar = SideBar()
        self.viewQVlayout = QVBoxLayout()

        self.viewQVlayout.addWidget(self.header)
        #self.viewQVlayout.addWidget(self.bookView)
        self.viewQVlayout.addStretch()
        self.viewQVlayout.setContentsMargins(0, 0, 0, 0)

        self.sidebar.profileBtn.clicked.connect(lambda: self.userProfileSwap("swap"))

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(self.viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)
        self.createBookView()

    def setUser(self, user):
        self.user = user
    
    def userProfileSwap(self, email: str):
        self.UserEmail.emit(email)
        
    def createBookView(self):
        self.bookView = BookView(range(1,fetchBookCount()+1))
        self.viewQVlayout.addWidget(self.bookView)