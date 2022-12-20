from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize
from gui.elements.bookView import BookView
from gui.elements.header import Header
from gui.elements.sidebar import SideBar
from database.dbfunctions import fetchAllBookIds


class LandingWindow(QFrame):
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

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.userid = id
