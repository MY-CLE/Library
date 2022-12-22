
class Account(object):
    def __init__(self, userid: int, firstname: str, lastname: str, phonenumber: int , email:str, password: str = '123', cpassword: str = '123'):
        self.__userid = userid
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phonenumber = phonenumber
        self.__email = email
        self.__password = password
        self.__cpassword = cpassword
    
    @property
    def userid(self):
        return self.__userid

    @userid.setter
    def userid(self, userid):
        self.__userid = userid
    
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def lastname(self):           
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def phonenumber(self):
        return self.__phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def cpassword(self):
        return self.__cpassword

    @cpassword.setter
    def cpassword(self, cpassword):
        self.__cpassword = cpassword

    @property
    def password_match(self) -> bool:
        return self.__password == self.__cpassword