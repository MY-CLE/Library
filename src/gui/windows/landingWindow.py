from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize, pyqtSignal
from gui.elements.bookView import BookView
from gui.elements.header import Header
from gui.elements.generalSidebar import SideBar
from database.dbfunctions import fetchAllBookIds


class LandingWindow(QFrame):
    UserEmail = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        self.userid = None
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("landingWindow")
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)

        self.header = Header()
        self.bookView = BookView(fetchAllBookIds())
        self.sidebar = SideBar()
        viewQVlayout = QVBoxLayout()

        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.bookView)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        self.sidebar.profileBtn.clicked.connect(lambda: self.userProfileSwap("f@p.de"))

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.userid = id
    
    def userProfileSwap(self, email: str):
        self.UserEmail.emit(email)