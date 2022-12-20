import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel, QFrame, QGridLayout)
from PyQt6.QtCore import QSize, Qt, pyqtSignal

from functional.account import Account
from database.dbfunctions import registerUser
class RegisterWindow(QFrame):
    
    newUser = pyqtSignal(Account)
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
        self.firstNameTextInput = QLineEdit()
        self.firstNameTextInput.setPlaceholderText("First Name")
        self.firstNameTextInput.setObjectName("firstNameTextInput")
        self.firstNameTextInput.setMaximumWidth(150)
        self.firstNameTextInput.setMinimumHeight(40)
        self.firstNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.lastNameTextInput = QLineEdit()
        self.lastNameTextInput.setPlaceholderText("Last Name")
        self.lastNameTextInput.setObjectName("lastNameTextInput")
        self.lastNameTextInput.setMaximumWidth(150)
        self.lastNameTextInput.setMinimumHeight(40)
        self.lastNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.phoneNumberTextInput = QLineEdit()
        self.phoneNumberTextInput.setPlaceholderText("Phone Number")
        self.phoneNumberTextInput.setObjectName("emailTextInput")
        self.phoneNumberTextInput.setMaximumWidth(150)
        self.phoneNumberTextInput.setMinimumHeight(40)
        self.phoneNumberTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.emailTextInput = QLineEdit()
        self.emailTextInput.setPlaceholderText("Email")
        self.emailTextInput.setObjectName("emailTextInput")
        self.emailTextInput.setMaximumWidth(150)
        self.emailTextInput.setMinimumHeight(40)
        self.emailTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.passwordTextInput = QLineEdit()
        self.passwordTextInput.setPlaceholderText("Password")
        self.passwordTextInput.setObjectName("passwordTextInput")
        self.passwordTextInput.setMaximumWidth(150)
        self.passwordTextInput.setMinimumHeight(40)
        self.passwordTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.passwordTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.passwordConfirmTextInput = QLineEdit()
        self.passwordConfirmTextInput.setPlaceholderText("Confirm Password")
        self.passwordConfirmTextInput.setObjectName("passwordTextInput")
        self.passwordConfirmTextInput.setMaximumWidth(150)
        self.passwordConfirmTextInput.setMinimumHeight(40)
        self.passwordConfirmTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.passwordConfirmTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        #Registration Button
        registerBtn = QPushButton()
        registerBtn.setFixedSize(250,50)
        registerBtn.setText("Create Account")
        registerBtn.setObjectName("registerBtn")
        registerBtn.clicked.connect(lambda: self.registerBtnPressed(self.firstNameTextInput.text(), self.lastNameTextInput.text(), self.phoneNumberTextInput.text(), self.emailTextInput.text(), self.passwordTextInput.text(), self.passwordConfirmTextInput.text()))

        #Login forwarding Button
        loginForwardingBtn = QPushButton()
        loginForwardingBtn.setText("Already have an Account? Sign in")
        loginForwardingBtn.setFixedSize(250,20)
        loginForwardingBtn.setObjectName("forwardingBtn")
        loginForwardingBtn.clicked.connect(lambda: self.loginForwardingBtnPressed())

        # The Widgets are conatined in a QWidget to create a white background for the visual effects
        container = QWidget()
        container.setObjectName("registerContainer")
        container.setFixedSize(400,300)
        container.setStyleSheet('background-color: white')
        
        containerLayout = QVBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        containerLayoutGrid = QGridLayout()
        containerLayoutGrid.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        loginForwardingBtnLayout = QVBoxLayout()
        loginForwardingBtnLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        containerLayoutGrid.addWidget(self.firstNameTextInput,0,0)
        containerLayoutGrid.addWidget(self.lastNameTextInput,0,1)
        containerLayoutGrid.addWidget(self.phoneNumberTextInput,1,0)
        containerLayoutGrid.addWidget(self.emailTextInput,1,1)
        containerLayoutGrid.addWidget(self.passwordTextInput,2,0)
        containerLayoutGrid.addWidget(self.passwordConfirmTextInput,2,1)

        loginForwardingBtnLayout.addWidget(registerBtn)
        loginForwardingBtnLayout.setSpacing(12)
        loginForwardingBtnLayout.addWidget(loginForwardingBtn)

        containerLayout.addWidget(title)
        containerLayout.setSpacing(12)
        containerLayout.addLayout(containerLayoutGrid)
        containerLayout.setSpacing(12)
        containerLayout.addLayout(loginForwardingBtnLayout)

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

    #this is a signal fierd by the loginForwardBtn pressed
    def loginForwardingBtnPressed(self):

        print("User already has an account")
        self.pageSwap.emit("PageSwap")

    def registerBtnPressed(self, firstname: str, lastname: str, phonenumber: int , email:str, password: str, cpassword: str):

        print(f"New User Registration {firstname},{lastname},{phonenumber},{email},{password},{cpassword}.")
        newUser = Account(firstname,lastname,phonenumber,email,password,cpassword)
        match = newUser.password_match
        try:
            if(match):
                registerUser(newUser)
                self.newUser.emit(newUser)
                self.passwordConfirmTextInput.setText('')
                self.passwordTextInput.setText('')
                self.emailTextInput.setText('')
                self.firstNameTextInput.setText('')
                self.lastNameTextInput.setText('')
                self.phoneNumberTextInput.setText('')
            else:
                raise ValueError
        except ValueError:
            print("Passwords do not match")
    