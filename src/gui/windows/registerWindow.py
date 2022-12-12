import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel, QFrame, QGridLayout)
from PyQt6.QtCore import QSize, Qt, pyqtSignal

from functional.account import Account
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
        firstNameTextInput = QLineEdit()
        firstNameTextInput.setPlaceholderText("First Name")
        firstNameTextInput.setObjectName("firstNameTextInput")
        firstNameTextInput.setMaximumWidth(150)
        firstNameTextInput.setMinimumHeight(40)
        firstNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        lastNameTextInput = QLineEdit()
        lastNameTextInput.setPlaceholderText("Last Name")
        lastNameTextInput.setObjectName("lastNameTextInput")
        lastNameTextInput.setMaximumWidth(150)
        lastNameTextInput.setMinimumHeight(40)
        lastNameTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        phoneNumberTextInput = QLineEdit()
        phoneNumberTextInput.setPlaceholderText("Phone Number")
        phoneNumberTextInput.setObjectName("emailTextInput")
        phoneNumberTextInput.setMaximumWidth(150)
        phoneNumberTextInput.setMinimumHeight(40)
        phoneNumberTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        emailTextInput = QLineEdit()
        emailTextInput.setPlaceholderText("Email")
        emailTextInput.setObjectName("emailTextInput")
        emailTextInput.setMaximumWidth(150)
        emailTextInput.setMinimumHeight(40)
        emailTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        passwordTextInput = QLineEdit()
        passwordTextInput.setPlaceholderText("Password")
        passwordTextInput.setObjectName("passwordTextInput")
        passwordTextInput.setMaximumWidth(150)
        passwordTextInput.setMinimumHeight(40)
        passwordTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        passwordTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        passwordConfirmTextInput = QLineEdit()
        passwordConfirmTextInput.setPlaceholderText("Confirm Password")
        passwordConfirmTextInput.setObjectName("passwordTextInput")
        passwordConfirmTextInput.setMaximumWidth(150)
        passwordConfirmTextInput.setMinimumHeight(40)
        passwordConfirmTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        passwordConfirmTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        #Registration Button
        registerBtn = QPushButton()
        registerBtn.setFixedSize(250,50)
        registerBtn.setText("Create Account")
        registerBtn.setObjectName("registerBtn")
        registerBtn.clicked.connect(lambda: self.registerBtnPressed(firstNameTextInput.text(), lastNameTextInput.text(), phoneNumberTextInput.text(), emailTextInput.text(), passwordTextInput.text(), passwordConfirmTextInput.text()))

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

        containerLayoutGrid.addWidget(firstNameTextInput,0,0)
        containerLayoutGrid.addWidget(lastNameTextInput,0,1)
        containerLayoutGrid.addWidget(phoneNumberTextInput,1,0)
        containerLayoutGrid.addWidget(emailTextInput,1,1)
        containerLayoutGrid.addWidget(passwordTextInput,2,0)
        containerLayoutGrid.addWidget(passwordConfirmTextInput,2,1)

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
                self.newUser.emit(newUser)
            else:
                raise ValueError
        except ValueError:
            print("Passwords do not match")
    