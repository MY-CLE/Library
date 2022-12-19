from gui.elements.detailsView import DetailsView
from gui.elements.header import Header
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize, Qt

from gui.elements.userDetailsSidebar import UserDetailsSidebar
from gui.elements.userDetailsView import UserDetailsView

class UserDetailsWindow(QFrame):
    def __init__(self,bookNo, parent=None):
        super(QFrame, self).__init__()
        self.bookNo = bookNo
        self.setWindowTitle("User Profile Details")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("userDetailsWindow")

        self.sidebar = UserDetailsSidebar()
        #self.sidebar.setFixedSize(250,500)
        self.userDetails = UserDetailsView()

        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.userDetails)
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar, Qt.AlignmentFlag.AlignLeft)
        mainQHlayout.addLayout(viewQVlayout, Qt.AlignmentFlag.AlignLeft)
        mainQHlayout.setContentsMargins(0, 150, 0, 100)

        self.setLayout(mainQHlayout)
