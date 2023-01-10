import sys
import unittest
sys.path.insert(0, "src//")
from gui.windows.loginWindow import LoginWindow


class LoginUnitTest(unittest.TestCase):
    
    def test_normal_input(self):
        """
        Test if the return functions work
        """
        login = LoginWindow.validateInput('peter.star@mail.com', 'star!?')
        self.assertEqual('peter.star@mail.com', login)
        self.assertEqual('star!?',login)
    
    def test_no_input(self):
        """
        If there are no User inputs assert error
        """
        
        with self.assertRaises(ValueError):
            LoginWindow.validateInput('','')
            
    def test_wrong_email(self):
        '''
        Raise error when not a real email adress as input
        '''
        emailList = ['@', '4', 'peter@star@mail.com', 'Ralph', '175824312', 'peters stars@mail.de' ]
        
        for email in emailList:
            with self.assertRaises(ValueError):
                login = LoginWindow.validateInput(email,'star!?')
                                
    def test_db_return_value(self):
        login = LoginWindow.validateInput('peter.star@mail.com', 'star!?')
        self.assertEqual(login,True)
        
            



if __name__ == '__main__':
    unittest.main()