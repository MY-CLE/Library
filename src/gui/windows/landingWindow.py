from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize
from gui.elements.header import Header
from gui.elements.libaryView import LibraryView
from gui.elements.sidebar import SideBar


class LandingWindow(QFrame):
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
        self.libraryView = LibraryView()
        self.sidebar = SideBar()
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.libraryView)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.userid = id