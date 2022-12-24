import sys
sys.path.insert(0, "src//")
from dataclasses import dataclass, field
from typing import List, Optional

from functional.rating import Rating
from database.dbconnect import DatabaseHandler
from datetime import date
from psycopg2 import Binary

@dataclass
class Book(object):
    id: int
    title: str
    author: str
    genre: str
    publishingYear: int
    publisher: str
    picture: str = field(default='')
    ratings: List[float] = field(default_factory=list)
    borrowedDate: Optional[date] = None
    isBorrowed:bool = field(default=False)

    @property
    def addRating(self, newRating: Rating) -> None:
        self.ratings.append(newRating)
    #currentRatings: Optional[float] = None

    # get average rating of a book rounded to an int.
    # added if/else to avoid divison by zero error, when there are no ratings.
    @property
    def getAverageRating(self) -> int:
        sum = 0
        if self.ratings == None:
            return 0
        else:
            for rating in self.ratings:
                sum += rating[0]
            return round(sum / len(self.ratings))


    def addToDatabase(self) -> None:
        databaseHandler = DatabaseHandler()
        databaseHandler.parser(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({self.__id}, '{self.__title}', '{self.__author}', '{self.__genre}', {self.__publishingYear}, '{self.__borrowedDate}', '{self.__publisher}', {self.getAverageRating()}, {self.__isBorrowed}, {(self.__picture)});")

 
    


#book = Book(100, "Rs", "TEST", 2001, "TESTEDITION", "PETERRIECHT", "GERUCH", str(date(2022, 12, 13)), Binary(bytearray(4)))
#book = Book(100, "Titel", "Author", "Genre", 2022, "Publisher", Binary(bytearray(4)), 5.0, date(2022, 12, 13))
#book.setBorrowed()
#book.addToDatabase()
#print(str(date(2022, 12, 13)))
#print(book)