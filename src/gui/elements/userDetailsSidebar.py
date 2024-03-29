import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QWidget,QLabel, QPushButton, QSpacerItem)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class UserDetailsSidebar(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('sideBar')
        self.setMinimumSize(250, 100)
        self.setMaximumSize(250, 3000)
        
        self.btnVLayout= QVBoxLayout()
        
        self.homeBtn = QPushButton()
        self.homeBtn.setObjectName('homeBtn')
        
        self.profileBtn = QPushButton()
        self.profileBtn.setObjectName('profilLabelBtn')
        #path = 'src/assets/icons/no_profile_pic.png'
        userPath = 'src/assets/icons/test-user-pic.png'
        self.profileBtn.setStyleSheet(f'border-image: url({userPath});')

        self.settingsBtn = QPushButton()
        self.settingsBtn.setObjectName('settingsBtn')
        
        self.logoutBtn = QPushButton()
        self.logoutBtn.setObjectName('logoutBtn')
        
        
        self.btnVLayout.addWidget(self.profileBtn)
        self.btnVLayout.addWidget(self.homeBtn)
        self.btnVLayout.addStretch()
        self.btnVLayout.addWidget(self.logoutBtn)
        self.btnVLayout.addWidget(self.settingsBtn)
        self.btnVLayout.addSpacing(30)

        btnLs = [self.profileBtn, self.homeBtn, self.logoutBtn, self.settingsBtn]

        for index, widget in enumerate(btnLs):
            widget.setFixedSize(60,60)
            
        
        #self.btnVLayout.addWidget(self.settingsBtn)
        
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addLayout(self.btnVLayout)
        self.setLayout(mainHoriLayout)