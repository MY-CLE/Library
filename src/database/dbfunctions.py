from .dbconnect import DatabaseHandler
from functional.book import Book

def userLogin(email, pwd) -> bool:
    sqlpass = DatabaseHandler()
    return sqlpass.parser(f"SELECT login('{email}','{pwd}')")[0][0]
   
def registerUser(emai, pwd, firstname, lastname, phonenumber):
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
           
def addToDatabase(book:Book) -> None:
        databaseHandler = DatabaseHandler()
        databaseHandler.parser(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({book.getID()}, '{book.getTitle()}', '{book.getAuthor()}', '{book.getGenre()}', {book.getPublishingYear()}, '{book.getBorrowedDate()}', '{book.getPublisher()}', {book.getAverageRating()}, {book.getIsBorrowed()}, '{book.getPicture()}');")
 
    
    