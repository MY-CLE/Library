import sys
sys.path.insert(0, "src//")
from datetime import date
from functional.book import Book
from database.dbconnect import DatabaseHandler

def updateBorrowedTable(borrowedId:int, userId:int, book:Book) -> None:
    db = DatabaseHandler()
    query = f"INSERT INTO isborrowed (borrowedid, bookid, userid, booktitle) VALUES ({borrowedId}, {book.getID()}, {userId}, '{book.getTitle()}');"
    db.insert(query)

#book = Book(3, "Faust", "TEST", 2001, "TESTEDITION", "PETERRIECHT", "GERUCH", str(date(2022, 12, 13)), False , "mein/path/stinkt")
#updateBorrowedTable(1, 1, book)

