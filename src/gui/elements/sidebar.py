from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QFrame, QPushButton, QSpacerItem )
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
        
        self.profilBtn = QPushButton()
        self.profilBtn.setObjectName('profilBtn')
        
        self.settingsBtn = QPushButton()
        self.settingsBtn.setObjectName('settingsBtn')
        
        self.logoutBtn = QPushButton()
        self.logoutBtn.setObjectName('logoutBtn')

        
        
        btnLs = [self.homeBtn, self.addBookBtn, self.profilBtn, 'Stretch', self.logoutBtn, self.settingsBtn]
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
    
        
    
        