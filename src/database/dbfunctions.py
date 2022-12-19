from .dbconnect import DatabaseHandler
from functional.book import Book

def userLogin(email, pwd) -> bool:
    sqlpass = DatabaseHandler()
    return sqlpass.parser(f"SELECT login('{email}','{pwd}')")[0][0]
   
def registeruser(emai, pwd, firstname, lastname, phonenumber):
    #TODO
    print(emai, pwd, firstname, lastname, phonenumber)
    
def fetchBook(bookId) -> Book:
    dh = DatabaseHandler()
    dbresult =  dh.parser(f"SELECT * FROM books WHERE bookid={bookId};")[0]
    print(*dbresult)
    return Book(*dbresult)

def fetchAllBookIds() -> list:
    dh = DatabaseHandler()
    return dh.parser(f"SELECT bookid FROM books;")[0][0]
           
    
    
    