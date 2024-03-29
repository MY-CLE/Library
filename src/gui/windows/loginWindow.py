import os
import re
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel, QFrame, QMessageBox)
from PyQt6.QtCore import QSize, Qt, pyqtSignal
from database.dbfunctions import userLogin, getUser
from functional.account import Account
# This Class displays a login page from which the user can login to his account
# It contains 2 Text Inputs and one login button, the forgotten password label is purely for visual
# after the LoginBtn is pressed a function is  called which communicates with the DB and returns a value
# after a successful login the this function calls a parent function to change the current displayed widgets

class LoginWindow(QFrame):
    
    sendUser = pyqtSignal(Account)
    pageSwap = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QFrame, self).__init__()
        # Keeps track of login status
        self.setWindowTitle("Login")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName('loginWindow')
        
        #Title 
        title = QLabel()
        title.setText("Login")
        title.setObjectName('loginTitle')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setMaximumHeight(40)
        
        #Forgotten Password Lable
        forgottenpwd = QLabel()
        forgottenpwd.setText("Forgotten Password?")
        forgottenpwd.setFixedSize(250,20)
        forgottenpwd.setAlignment(Qt.AlignmentFlag.AlignBottom)
        forgottenpwd.setObjectName("forgottenpwdLable")

        
        #Textinput
        self.emailTextInput = QLineEdit()
        self.emailTextInput.setPlaceholderText("Email")
        self.emailTextInput.setObjectName("emailTextInput")
        self.emailTextInput.setMaximumWidth(250)
        self.emailTextInput.setMinimumHeight(40)
        self.emailTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.emailTextInput.returnPressed.connect(lambda: self.loginBtnPressed(self.emailTextInput.text(), self.passwordTextInput.text()))
        
        self.passwordTextInput = QLineEdit()
        self.passwordTextInput.setPlaceholderText("Password")
        self.passwordTextInput.setObjectName("passwordTextInput")
        self.passwordTextInput.setMaximumWidth(250)
        self.passwordTextInput.setMinimumHeight(40)
        self.passwordTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.passwordTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.passwordTextInput.returnPressed.connect(lambda: self.loginBtnPressed(self.emailTextInput.text(), self.passwordTextInput.text()))

        #Login Button
        loginBtn = QPushButton()
        loginBtn.setFixedSize(250,50)
        loginBtn.setObjectName("loginBtn")
        loginBtn.setText("Login")
        loginBtn.clicked.connect(lambda: self.loginBtnPressed(self.emailTextInput.text(), self.passwordTextInput.text()))
        
        #Registration forwarding Button
        registerForwardingBtn = QPushButton()
        registerForwardingBtn.setText("No Account? Register here")
        registerForwardingBtn.setFixedSize(250,20)
        #registerBtn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        registerForwardingBtn.setObjectName("forwardingBtn")
        registerForwardingBtn.clicked.connect(lambda: self.registerBtnPressed())

        # The Widgets are contained in a QWidget to create a white background for the visual effects
        container = QWidget()
        container.setObjectName("loginContainer")
        container.setFixedSize(400,300)
        container.setStyleSheet('background-color: white')
        
        containerLayout = QVBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        containerLayout.addWidget(title)
        containerLayout.addSpacing(12)
        containerLayout.addWidget(self.emailTextInput)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(self.passwordTextInput)
        containerLayout.addWidget(forgottenpwd)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(loginBtn)        
        containerLayout.addWidget(registerForwardingBtn)
            
        container.setLayout(containerLayout)
        
        # The container is wrapped in a Vertical BoxLayout to keep it in the middle
        
        #The logo is loaded from the assets folder
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/logo/hse-library-logo-smaller-removebg.png'))
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
    
    #returns loginStatus as an integer
    def isLogedIn(self):
        return int(self.loginStatus)
    
    
    #this is a signal fired by the loginBtnPressed
    def loginBtnPressed(self, email: str, pwd: str):
            if self.validateInput(email, pwd):
                userid = userLogin(email, pwd)[0][0]
                print(userid)
                if userid> 0:
                    user = getUser(userid)
                    self.sendUser.emit(user)
                    self.emailTextInput.setText('')
                    self.passwordTextInput.setText('')
                else:
                    msgbox = QMessageBox.information(self, "Invalid Login", "You used a invalid emailaddress, password combination")
                

    #this is a signal fierd by the registerBtnPressed
    def registerBtnPressed(self):

        print("User Registration")
        self.pageSwap.emit("PageSwap")
    
    
    
    def validateInput (self, email, password):
        try:
            if (email == '') or (password == ''):
                raise ValueError
        except ValueError as e:
            msg = QMessageBox.information(self, "Invalid Login", "You need to give a username and password to login")
            return False
        
        try:
            filter_email = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            if filter_email.findall(email) == []:
                raise ValueError
        except ValueError as e:
            msg = QMessageBox.information(self, "Invalid Login", "You need to give a valid Email address")
            return False
        
        return True
            