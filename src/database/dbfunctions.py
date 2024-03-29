import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book
from functional.account import Account

from datetime import datetime

def userLogin(email:str, pwd: str) -> bool:
    return DatabaseHandler().parser(f"SELECT login('{email}','{pwd}')")
   
def registerUser(user: Account):
    DatabaseHandler().insert(f"INSERT INTO credentials (firstname, lastname, phonenumber, email, password) VALUES ('{user.firstname}','{user.lastname}','{user.phonenumber}','{user.email}','{user.password}');")

def getUser(userId: str) -> Account:
    try:
        if(userId):
            return Account(*DatabaseHandler().parser(f"SELECT userid, firstname, lastname, phonenumber, email FROM public.user WHERE userid='{userId}';")[0])
        else:
            raise AttributeError
    except (IndexError, AttributeError):
        print("Email nicht in der DB vorhanden")    
def fetchBook(bookId) -> Book:
    return Book(*DatabaseHandler().parser(f"SELECT * FROM books WHERE bookid={bookId};")[0])

def fetchAllBookIds() -> list:
    return DatabaseHandler().parser(f"SELECT bookid FROM books;")[0][0]
def fetchBookCount()-> int:
    return DatabaseHandler().parser(f"SELECT Count(*) FROM books;")[0][0]
           
def addToDatabase(book:Book) -> None:
    DatabaseHandler().insert(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({book.getID()}, '{book.getTitle()}', '{book.getAuthor()}', '{book.getGenre()}', {book.getPublishingYear()}, '{book.getBorrowedDate()}', '{book.getPublisher()}', {book.getAverageRating()}, {book.getIsBorrowed()}, '{book.getPicture()}');")
 
def insertBorrowedTable(user:Account, book:Book) -> None:
    if DatabaseHandler().parser(f'SELECT * FROM isborrowed WHERE bookid={book.getID()} AND userid={user.userid}') == []:
        DatabaseHandler().insert(f"INSERT INTO isborrowed (bookid, userid) VALUES ({book.getID()},{user.userid});")

#add opposite borrowed status of book and current timestamp as borrowed date to db.
def changeBorrowedStatus(book: Book, newStatus) -> None:
    update = f"UPDATE books SET isborrowed={newStatus},borroweddate=current_timestamp WHERE bookid={book.getID()}"
    DatabaseHandler().insert(update)
    
def updateBooksTable() -> None:
    DatabaseHandler()

def checkisBorrowedTable(bookId):
    res =  DatabaseHandler().parser(f"SELECT userId FROM isborrowed where bookid={bookId}")
    if  not res:
        return 0
    return res[0][0]
    
def removeBorrowedTable(book:Book) -> None:
    DatabaseHandler().insert(f"DELETE FROM isborrowed WHERE bookid = {book.getID()};")

def getborrowedBookIdsByUser(user: Account):
    res = DatabaseHandler().parser(f"SELECT bookid FROM isborrowed WHERE userid = {user.userid}")
    formatedResult = []
    for item in res:
        formatedResult.append(item[0])
    return formatedResult
    

#test = fetchBook(1)
#changeBorrowedStatus(test)
#print(test)