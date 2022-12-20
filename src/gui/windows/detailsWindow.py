from gui.elements.detailsView import DetailsView
from gui.elements.header import Header
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize

from gui.elements.sidebar import SideBar


class DetailWindow(QFrame):
    def __init__(self, book, parent=None):
        super(QFrame, self).__init__()
        self.book = book
        self.setWindowTitle("Details")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("detailsWindow")

        self.sidebar = SideBar()
        self.header = Header()
        self.details = DetailsView(book)
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.header)
        viewQVlayout.addWidget(self.details)
        viewQVlayout.addStretch()
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(mainQHlayout)
