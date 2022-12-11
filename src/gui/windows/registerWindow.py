import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel, QFrame)
from PyQt6.QtCore import QSize, Qt, pyqtSignal


class RegisterWindow(QFrame):
    
    pageSwap = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        # Keeps track of login status
        self.setWindowTitle("Registration")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName('registerWindow')
        
        #Title 
        title = QLabel()
        title.setText("Registration")
        title.setObjectName('registrationTitle')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setMaximumHeight(40)
    
        
        #Textinput
        firstNameTextInput = QLineEdit()
        firstNameTextInput.setPlaceholderText("First Name")
        firstNameTextInput.setObjectName("firstNameTextInput")
        firstNameTextInput.setMaximumWidth(250)
        firstNameTextInput.setMinimumHeight(40)
        firstNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        lastNameTextInput = QLineEdit()
        lastNameTextInput.setPlaceholderText("Last Name")
        lastNameTextInput.setObjectName("lastNameTextInput")
        lastNameTextInput.setMaximumWidth(250)
        lastNameTextInput.setMinimumHeight(40)
        lastNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        emailTextInput = QLineEdit()
        emailTextInput.setPlaceholderText("Email")
        emailTextInput.setObjectName("emailTextInput")
        emailTextInput.setMaximumWidth(250)
        emailTextInput.setMinimumHeight(40)
        emailTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        passwordTextInput = QLineEdit()
        passwordTextInput.setPlaceholderText("Password")
        passwordTextInput.setObjectName("passwordTextInput")
        passwordTextInput.setMaximumWidth(250)
        passwordTextInput.setMinimumHeight(40)
        passwordTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        passwordTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        
        #Registration Button
        loginBtn = QPushButton()
        loginBtn.setText("Already have an Account? Sign in")
        loginBtn.setFixedSize(250,20)
        #registerBtn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        loginBtn.setObjectName("registerBtn")
        loginBtn.clicked.connect(lambda: self.loginBtnPressed())

        # The Widgets are conatined in a QWidget to create a white background for the visual effects
        container = QWidget()
        container.setObjectName("loginContainer")
        container.setFixedSize(400,300)
        container.setStyleSheet('background-color: white')
        
        containerLayout = QVBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        containerLayout.addWidget(title)
        containerLayout.addSpacing(12)
        containerLayout.addWidget(firstNameTextInput)
        containerLayout.addWidget(lastNameTextInput)
        containerLayout.addWidget(emailTextInput)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(passwordTextInput)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(loginBtn)
            
        container.setLayout(containerLayout)
        
        # The container is wrapped in a Vertical BoxLayout to keep it in the middle
        
        #The logo is loaded from the assets folder
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/Logo/hse-library-logo-smaller-removebg-preview.png'))
        logoLable.setPixmap(logo)
        
        logoHLayout = QHBoxLayout()
        logoHLayout.addStretch()
        logoHLayout.addWidget(logoLable)
        logoHLayout.addStretch()
        
        containerHLayot = QHBoxLayout()
        containerHLayot.addStretch()
        containerHLayot.addWidget(container)
        containerHLayot.addStretch()
        
        mainVertLayot = QVBoxLayout()
        mainVertLayot.addStretch()
        mainVertLayot.addLayout(logoHLayout)
        mainVertLayot.addLayout(containerHLayot)
        mainVertLayot.addStretch()
        
        
        self.setLayout(mainVertLayot)

    #this is a signal fierd by the loginBtnPressed
    def loginBtnPressed(self):

        print("User already has an account")
        self.pageSwap.emit("PageSwap")
    