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
        self.container.setMinimumSize(800, 100)
        self.container.setMaximumSize(3000, 3000)
        self.container.setStyleSheet('background-color: white;')

        #self.container.setBaseSize(600,600)

        self.labelContainer = QWidget()
        self.labelContainer.setObjectName('userDetailsViewContainer')
        self.labelContainer.setMinimumSize(100,100)
        self.labelContainer.setStyleSheet('background-color: gray;')


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


        #self.containerVerticalLayout.addWidget(self.title)
        #self.containerVerticalLayout.stretch(5)
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

        self.labelContainer.setLayout(self.containerVerticalLayout)

        self.containerHorizontalLayout = QHBoxLayout()
        self.containerHorizontalLayout.addWidget(self.labelContainer)


        self.container.setLayout(self.containerHorizontalLayout)

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(verticalLayout)