from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize, pyqtSignal
from gui.elements.bookView import BookView
from gui.elements.header import Header
from gui.elements.generalSidebar import SideBar
from database.fetchAllBookIds import fetchBooks

class LandingWindow(QFrame):
    UserProfile = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        self.userid = None
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("landingWindow")
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        #self.setContentsMargins(0,0,0,0)

        self.header = Header()
        fb = fetchBooks
        
        self.bookView = BookView(fb.fetchAllBooks())
        self.sidebar = SideBar()
        viewQVlayout = QVBoxLayout()

        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.bookView)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        self.sidebar.profileBtn.clicked.connect(lambda: self.userProfileSwap("1"))

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.userid = id
    
    def userProfileSwap(self,text):
        self.UserProfile.emit(text)