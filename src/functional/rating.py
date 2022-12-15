import sys
sys.path.insert(0, "src//")
from functional.illegalRatingError import IllegalRatingError


class Rating(object):

    def __init__(self, value: int) -> None:
        if((value > 5) or (value < 0)):
            raise IllegalRatingError()
        else :
            self.__value = value

    def getValue(self) -> int:
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)

