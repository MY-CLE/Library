class IllegalRatingError(Exception):
    
    def __init__(self) -> None:
        super().__init__("Ratings are only allowed from 0 to 5 stars.")