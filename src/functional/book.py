import sys
sys.path.insert(0, "src//")
from functional.rating import Rating
from database.dbconnect import DatabaseHandler
from datetime import date
from psycopg2 import Binary
#from rating import rating


class Book(object):

    def __init__(self, id: int, title: str, author: str, genre: str, publishingYear: int, 
    borrowedDate: date, publisher: str, ratings: float, isBorrowed:bool, picture: str) -> None:
        self.__id = id
        self.__title = title
        self.__author = author
        self.__publishingYear = publishingYear
        self.__publisher = publisher
        self.__currentRatings= ratings
        self.__ratings: ratings = []
        self.__isBorrowed= isBorrowed
        self.__genre = genre
        self.__borrowedDate = borrowedDate
        self.__picture = picture
        
          
    def getID(self) -> id:
        return self.__id
    
    def setID(self, id: int) -> None:
        self.__id = id

    def getTitle(self) -> str:
        return self.__title

    def setTitle(self, title: str) -> None:
        self.__title = title

    def getAuthor(self) -> str:
        return self.__author

    def setAuthor(self, author: str) -> None:
        self.__author = author

    def getPublishingYear(self) -> int:
        return self.__publishingYear

    def setPublishingYear(self, publishingYear: int) -> None:
        self.__publishingYear = publishingYear

    def getPublisher(self) -> str:
        return self.__publisher

    def setPublisher(self, publisher: str) -> None:
        self.__publisher = publisher

    def getRatingColumnValue(self) -> float:
        return self.__currentRatings

    def getRatings(self) -> list:
        return self.__ratings

    def addRating(self, newRating: Rating) -> None:
        self.__ratings.append(newRating)

    # get average rating of a book rounded to an int.
    # added if/else to avoid divison by zero error, when there are no ratings.
    def getAverageRating(self) -> int:
        sum = 0
        if(len(self.__ratings) == 0):
            return 0
        else:
            for rating in self.__ratings:
                sum += rating.getValue()
            return round(sum / len(self.__ratings))

    def isBorrowed(self) -> bool:
        return self.__isBorrowed

    def getGenre(self) -> str:
        return self.__genre

    def setGenre(self, genre: str) -> str:
        self.__genre = genre

    def getBorrowedDate(self) -> str:
        return str(self.__borrowedDate)

    def setBorrowedDate(self, borrowedDate: date) -> None:
        self.__borrowedDate = borrowedDate
        
    def getIsBorrowed(self) -> bool:
        return self.__isBorrowed
    
    def seBorrowedStatus(self, newBorrowedStatus: bool):
        self.__isBorrowed = newBorrowedStatus

    def getPicture(self) -> str:
        return self.__picture

    def setPicture(self, picture: str) -> None:
        self.__picture = picture

    def addToDatabase(self) -> None:
        databaseHandler = DatabaseHandler()
        databaseHandler.parser(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({self.__id}, '{self.__title}', '{self.__author}', '{self.__genre}', {self.__publishingYear}, '{self.__borrowedDate}', '{self.__publisher}', {self.getAverageRating()}, {self.__isBorrowed}, {(self.__picture)});")

    def __str__(self) -> str:
        return str(self.getID()) + " " + str(self.getTitle()) + " " + str(self.getAuthor()) + " " +str(self.getGenre()) + " " +str(self.getPublishingYear()) + " " +str(self.getBorrowedDate()) + " " +str(self.getRatingColumnValue()) + " " +str(self.getIsBorrowed()) +" " + str(self.getPicture())
 
    


#book = Book(100, "Rs", "TEST", 2001, "TESTEDITION", "PETERRIECHT", "GERUCH", str(date(2022, 12, 13)), Binary(bytearray(4)))
#book.setBorrowed()
#book.addToDatabase()
print(str(date(2022, 12, 13)))