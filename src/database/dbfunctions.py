import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book
from functional.account import Account

from datetime import datetime

def userLogin(user) -> bool:
    return DatabaseHandler().parser(f"SELECT login('{user.email}','{user.password}')")[0][0]
   
def registerUser(user):
    DatabaseHandler().insert(f"INSERT INTO credentials (firstname, lastname, phonenumber, email, password) VALUES ('{user.firstname}','{user.lastname}','{user.phonenumber}','{user.email}','{user.password}');")

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
    DatabaseHandler().insert(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({book.getID()}, '{book.getTitle()}', '{book.getAuthor()}', '{book.getGenre()}', {book.getPublishingYear()}, '{book.getBorrowedDate()}', '{book.getPublisher()}', {book.getAverageRating()}, {book.getIsBorrowed()}, '{book.getPicture()}');")
 
def insertBorrowedTable(borrowedId:int, userId:int, book:Book) -> None:
    query = f"INSERT INTO isborrowed (borrowedid, bookid, userid, booktitle) VALUES ({borrowedId}, {book.getID()}, {userId}, '{book.getTitle()}');"
    DatabaseHandler().insert(query)

#add opposite borrowed status of book and current timestamp as borrowed date to db.
def changeBorrowedStatus(book: Book) -> None:
    update = f"UPDATE books SET isborrowed={not book.getIsBorrowed()},borroweddate=current_timestamp WHERE bookid={book.getID()}"
    DatabaseHandler().insert(update)
    
def updateBooksTable() -> None:
    DatabaseHandler()

def removeBorrowedTable(borrowedId:int) -> None:
    query = f"DELETE FROM isborrowed WHERE borrowedid = {borrowedId};"
    DatabaseHandler().insert(query)

test = fetchBook(1)
changeBorrowedStatus(test)
print(test)
#book = Book(3, "Faust", "TEST", 2001, "TESTEDITION", "PETERRIECHT", "GERUCH", str(date(2022, 12, 13)), False , "mein/path/stinkt")
#insertBorrowedTable(1, 1, book)
#removeBorrowedTable(1)
