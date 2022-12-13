import sys
sys.path.insert(0, "src//")
from functional.rating import Rating
#from rating import rating


class Book(object):

    def __init__(self, title: str, author: str, publishingYear: int, edition: str, publisher: str) -> None:
        self.__title = title
        self.__author = author
        self.__publishingYear = publishingYear
        self.__edition = edition
        self.__publisher = publisher
        self.__ratings: Rating = []
        self.__isBorrowed: bool = False

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

    def getEdition(self) -> str:
        return self.__edition

    def setEdition(self, edition: str) -> None:
        self.__edition = edition

    def getPublisher(self) -> str:
        return self.__publisher

    def setPublisher(self, publisher: str) -> None:
        self.__publisher = publisher

    def getRatings(self) -> list:
        return self.__ratings

    def addRating(self, newRating: Rating) -> None:
        self.__ratings.append(newRating)

    # get average rating of a book rounded to an int.
    def getAverageRating(self) -> int:
        sum = 0
        for rating in self.__ratings:
            sum += rating.getValue()
        return round(sum / len(self.__ratings))

    def isBorrowed(self) -> bool:
        return self.__isBorrowed
    
    def setBorrowed(self) -> None:
        self.__isBorrowed = True
    
    def setUnBorrowed(self) -> None:
        self.__isBorrowed = False



book = Book("egal", "egal", 2001, "gal", "egal")
for i in range(0, 6):
    book.addRating(Rating(i))
    print(book.getAverageRating())
    


