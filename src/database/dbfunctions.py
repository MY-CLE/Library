from .dbconnect import DatabaseHandler
from functional.book import Book

def userLogin(email, pwd) -> bool:
    return DatabaseHandler().parser(f"SELECT login('{email}','{pwd}')")[0][0]
   
def registeruser(emai, pwd, firstname, lastname, phonenumber):
    #TODO
    print(emai, pwd, firstname, lastname, phonenumber)
    
def fetchBook(bookId) -> Book:
    return Book(*DatabaseHandler().parser(f"SELECT * FROM books WHERE bookid={bookId};")[0])

def fetchAllBookIds() -> list:
    return DatabaseHandler().parser(f"SELECT bookid FROM books;")[0][0]
           
    
    
    