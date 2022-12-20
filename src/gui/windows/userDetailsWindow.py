from gui.elements.detailsView import DetailsView
from gui.elements.header import Header
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame)
from PyQt6.QtCore import QSize, Qt, pyqtSignal

from gui.elements.userDetailsSidebar import UserDetailsSidebar
from gui.elements.userDetailsView import UserDetailsView

class UserDetailsWindow(QFrame):

    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent)
        self.firstanme = None
        self.lastname = None
        self.email = None
        self.lastLogin = None
        self.phonenumber = None

        self.setWindowTitle("User Profile Details")
        self.setMinimumSize(QSize(1080, 720))
        self.setObjectName("userDetailsWindow")


        self.sidebar = UserDetailsSidebar()
        self.userDetails = UserDetailsView()

        #self.userDetails.firstnameUserDetailsOutput.setText(str(self.firstanme))
        self.userDetails.lastnameUserDetailsOutput.setText(str(self.lastname))
        self.userDetails.emailUserDetailsOutput.setText(str(self.email))
        self.userDetails.lastLoginUserDetailsOutput.setText(str(self.lastLogin))
        self.userDetails.phonenumberUserDetailsOutput.setText(str(self.phonenumber))

        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(self.userDetails)
        viewQVlayout.setContentsMargins(0, 0, 0, 0)

        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(self.sidebar)
        mainQHlayout.addWidget(self.userDetails)
        mainQHlayout.setContentsMargins(0, 100, 0, 30)

        self.setLayout(mainQHlayout)

    def setUserid(self, id):
        self.firstname = id
        self.userDetails.firstnameUserDetailsOutput.setText(str(self.firstanme))