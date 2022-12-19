import os
from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QWidget,QLabel, QPushButton, QSpacerItem)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
class SideBar(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('sideBar')
        self.setFixedWidth(100)
        
        self.btnVLayout= QVBoxLayout()
        
        self.homeBtn = QPushButton()
        self.homeBtn.setObjectName('homeBtn')
        
        self.addBookBtn = QPushButton()
        self.addBookBtn.setObjectName('addBookBtn')
        
        self.profileBtn = QPushButton()
        self.profileBtn.setObjectName('profilLabelBtn')
        #path = 'src/assets/icons/no_profile_pic.png'
        userPath = 'src/assets/icons/test-user-pic.png'
        self.profileBtn.setStyleSheet(f'border-image: url({userPath});')

        """ picPath = QPixmap(os.path.abspath('src/assets/icons/test-user-pic.png'))
        picPath.scaledToHeight(100)
        self.profilBtn.setPixmap(picPath)
        self.profilBtn.setMask(picPath.mask()) """
        
        self.settingsBtn = QPushButton()
        self.settingsBtn.setObjectName('settingsBtn')
        
        self.logoutBtn = QPushButton()
        self.logoutBtn.setObjectName('logoutBtn')
        
        
        btnLs = [self.profileBtn, self.homeBtn, self.addBookBtn, 'Stretch', self.logoutBtn, self.settingsBtn]
        #self.btnVLayout.addSpacing(30)
        for index, widget in enumerate(btnLs):
            if index == 3:
                self.btnVLayout.addStretch()
                continue
            widget.setFixedSize(60,60)
            self.btnVLayout.addWidget(widget)
            if index == len(btnLs)-1:
                continue
            self.btnVLayout.addSpacing(30)
            

        
        #self.btnVLayout.addWidget(self.settingsBtn)
        
        mainHoriLayout = QHBoxLayout()
        mainHoriLayout.addLayout(self.btnVLayout)
        self.setLayout(mainHoriLayout)
    
        
    
        