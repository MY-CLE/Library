import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book
from functional.account import Account

def userLogin(email, pwd) -> bool:
    return DatabaseHandler().parser(f"SELECT login('{email}','{pwd}')")[0][0]
   
def registerUser(email, pwd, firstname, lastname, phonenumber):
    #TODO
    print(email, pwd, firstname, lastname, phonenumber)

def getUser(email: str):
    try:
        if(email):
            return Account(*DatabaseHandler().parser(f"SELECT firstname, lastname, phonenumber, email FROM public.user WHERE email='{email}';")[0])
        else:
            raise AttributeError
    except (IndexError, AttributeError):
        print("Email nicht in der DB vorhanden")
    
def fetchBook(bookId) -> Book:
    return Book(*DatabaseHandler().parser(f"SELECT * FROM books WHERE bookid={bookId};")[0])

def fetchAllBookIds() -> list:
    return DatabaseHandler().parser(f"SELECT bookid FROM books;")[0][0]
           
def addToDatabase(book:Book) -> None:
    DatabaseHandler().parser(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({book.getID()}, '{book.getTitle()}', '{book.getAuthor()}', '{book.getGenre()}', {book.getPublishingYear()}, '{book.getBorrowedDate()}', '{book.getPublisher()}', {book.getAverageRating()}, {book.getIsBorrowed()}, '{book.getPicture()}');")
 
def updateBorrowedTable(borrowedId:int, userId:int, book:Book) -> None:
    query = f"INSERT INTO isborrowed (borrowedid, bookid, userid, booktitle) VALUES ({borrowedId}, {book.getID()}, {userId}, '{book.getTitle()}');"
    DatabaseHandler().insert(query)
    
def updateBooksTable() -> None:
    DatabaseHandler()