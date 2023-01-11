from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame, QLabel)
from PyQt6.QtCore import QSize
from database.dbfunctions import getborrowedBookIdsByUser
from functional.account import Account
from gui.elements.bookView import BookView
from gui.elements.header import Header
from gui.elements.generalSidebar import SideBar
class BorrowedBooksWindow(QFrame):
    def __init__(self, user: Account, parent=None):
        super(QFrame, self).__init__()
        self.user= user
        self.borrowedBookIds = getborrowedBookIdsByUser(self.user)
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
        self.title = QLabel()
        self.title.setObjectName('borrowedBooksTitle')
        self.title.setText(f'Your Borrowed Books:')
        self.viewQVlayout.addWidget(self.title)
        self.title.setContentsMargins(10,0,0,0)
        self.subTitle = QLabel()
        self.subTitle.setObjectName('borrowedBooksSubTitle')
        self.subTitle.setContentsMargins(10,0,0,0)
        self.subTitle.setText(f'you currently borrowing {len(self.borrowedBookIds)} books')
        self.viewQVlayout.addWidget(self.subTitle)
        self.createBookView()

    def setUser(self, user):
        self.user = user
    
    def userProfileSwap(self, email: str):
        self.UserEmail.emit(email)
        
    def  createBookView(self):
        self.bookView = BookView(self.borrowedBookIds,False)
        self.viewQVlayout.addWidget(self.bookView)