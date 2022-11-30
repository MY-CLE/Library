import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
import re
class Login(object):
    
        logincheck = False
        
        def __init__(self, email:str, password:str):
            if (email == '') or (password == ''):
                raise ValueError
            
            filter_email = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            if filter_email.findall(email) == []:
                raise ValueError

            self.__email = email
            self.__password = password

                
        def get_password(self) -> str:
            return self.__password
        
        def get_email(self) -> str:
            return self.__email

        def userlogin(self) -> int:
            sqlpass = DatabaseHandler()
            
            #add sql logic
            
            self.__logincheckingfunc = f"SELECT login('{self.get_email()}','{self.get_password()}')"
            return sqlpass.parser(self.__logincheckingfunc)[0][0]
        
        def user_login2(self) -> bool:
            db = DatabaseHandler()
            query = f"SELECT login('{self.get_email()}','{self.get_password()}')"
            return db.parser(query)
        
            
                
def main():
    a = Login("peter@riecht.com","meinPassword")
    print(a.userlogin())
    #print(a.user_login2())
    
        
if __name__ == '__main__':
    main()