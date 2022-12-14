import re
import database.dbconnect as db
class Login(object):
    
        logincheck = False
        
        def __init__(self, email:str, password:str):
            self._email = email
            self._password = password
                
        def get_password(self) -> str:
            return self._password
        
        def get_email(self) -> str:
            return self._email

        def userloginId(self) -> int:
            sqlpass = db.DatabaseHandler()
            #add sql logic
            self._logincheckingfunc = f"SELECT login('{self.get_email()}','{self.get_password()}')"
            return sqlpass.parser(self._logincheckingfunc)[0]
        
            
                
def main():
    a = Login("peter@riecht.com","meinPassword")
    print(a.userloginId())
    
        
if __name__ == '__main__':
    main()