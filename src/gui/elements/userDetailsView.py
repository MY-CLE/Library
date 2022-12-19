import os
from PyQt6.QtWidgets import (
    QHBoxLayout, QLayout, QVBoxLayout, QFrame, QWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage

class UserDetailsView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('userDetailsView')

        self.container = QWidget()
        self.container.setObjectName('userDetailsViewContainer')
        self.container.setMinimumSize(1000,600)

        #self.container.setBaseSize(600,600)

        """ self.textContainer = QWidget()
        self.textContainer.setObjectName('userDetailsViewContainer')
        self.textContainer.setMinimumWidth(200)
        self.textContainer.setMaximumHeight(300) """

        self.title = QLabel()
        self.title.setText("ACCOUNT")

        #Firstname
        self.firstnameUserDetails = QLabel()
        self.firstnameUserDetails.setObjectName('transparentUserDetails')
        self.firstnameUserDetails.setText("Firstname")

        self.firstnameUserDetailsOutput = QLabel()
        self.firstnameUserDetailsOutput.setObjectName('transparentUserDetailsOutput')
        self.firstnameUserDetailsOutput.setText("-")

        #Lastname
        self.lastnameUserDetails = QLabel()
        self.lastnameUserDetails.setObjectName('transparentUserDetails')
        self.lastnameUserDetails.setText("Lastname")

        self.lastnameUserDetailsOutput = QLabel()
        self.lastnameUserDetailsOutput.setObjectName('transparentUserDetailsOutput')
        self.lastnameUserDetailsOutput.setText("-")

        #Email Address
        self.emailUserDetails = QLabel()
        self.emailUserDetails.setObjectName('transparentUserDetails')
        self.emailUserDetails.setText("Email")

        self.emailUserDetailsOutput = QLabel()
        self.emailUserDetailsOutput.setObjectName('transparentUserDetailsOutput')
        self.emailUserDetailsOutput.setText("-")

        #Last Login Date
        self.lastLoginUserDetails = QLabel()
        self.lastLoginUserDetails.setObjectName('transparentUserDetails')
        self.lastLoginUserDetails.setText("Last Login")

        self.lastLoginUserDetailsOutput = QLabel()
        self.lastLoginUserDetailsOutput.setObjectName('transparentUserDetailsOutput')
        self.lastLoginUserDetailsOutput.setText("-")

        #Phone Number
        self.phonenumberUserDetails = QLabel()
        self.phonenumberUserDetails.setObjectName('transparentUserDetails')
        self.phonenumberUserDetails.setText("Phone Number")

        self.phonenumberUserDetailsOutput = QLabel()
        self.phonenumberUserDetailsOutput.setObjectName('transparentUserDetailsOutput')
        self.phonenumberUserDetailsOutput.setText("-")


        self.containerVerticalLayout = QVBoxLayout()
        #self.containerVerticalLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        self.containerVerticalLayout.addWidget(self.title)
        self.containerVerticalLayout.setSpacing(20)
        self.containerVerticalLayout.addWidget(self.firstnameUserDetails)
        self.containerVerticalLayout.addWidget(self.firstnameUserDetailsOutput)
        self.containerVerticalLayout.addWidget(self.lastnameUserDetails)
        self.containerVerticalLayout.addWidget(self.lastnameUserDetailsOutput)
        self.containerVerticalLayout.addWidget(self.emailUserDetails)
        self.containerVerticalLayout.addWidget(self.emailUserDetailsOutput)
        self.containerVerticalLayout.addWidget(self.lastLoginUserDetails)
        self.containerVerticalLayout.addWidget(self.lastLoginUserDetailsOutput)
        self.containerVerticalLayout.addWidget(self.phonenumberUserDetails)
        self.containerVerticalLayout.addWidget(self.phonenumberUserDetailsOutput)

        self.container.setLayout(self.containerVerticalLayout)

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(verticalLayout)