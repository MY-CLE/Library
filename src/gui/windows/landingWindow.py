from gui.elements.borrowedView import BorrowedView
from gui.elements.header import CustHeader
from gui.elements.libaryView import LibraryView
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize


class LandingWindow(QFrame):
    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        self.userid = None
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("landingWindow")
        self.setFrameShape(QFrame.Shape.NoFrame)
        # self.setLineWidth(0)

        self.header = CustHeader()
        self.libraryView = LibraryView()
        self.borrowedView = BorrowedView()
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.libraryView)
        viewQVlayout.addWidget(self.borrowedView)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.userid = id
        print(f'Landing Page User id ${self.userid}')
        self.borrowedView.bookView.updateUser(self.userid)
