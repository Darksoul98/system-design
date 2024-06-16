
from enum import Enum
from typing import Dict, List


class City:
    pass

class Movie:
    id: int
    name: str
    duration: int

class MovieController:
    # has a movie, keeps city wise movies
    cityMovies: Dict[City, List[Movie]]
    allMovies: List[Movie]
    
    # add crud methods
    
class SeatCategory(Enum):
    SILVER = "SILVER"
    GOLD = "GOLD"
    
class Seat:
    id: int
    row: int
    seatCategory: SeatCategory

class Screen:
    id: int
    dimensions: str
    # has seats
    seats: List[Seat]
    
    
class Show:
    id: int
    # Has movie detail
    movie: Movie
    # Has screen info
    screen: Screen
    startTime: int
    bookedSeatIds: List[int]
    
class Theatre:
    id: int
    address: str
    city: City
    screens: List[Screen]
    show: List[Show]
    
class TheatreController:
    cityTheatre: Dict[City, List[Theatre]]
    allTheatre: List[Theatre]

class Payment:
    pass

class Booking:
    show: Show
    seats: List[Seat]
    payment: Payment
    
    
class BookMyShow:
    movieController: MovieController
    theatreController: TheatreController
    
    def __init__(self) -> None:
        self.movieController = MovieController()
        self.theatreController = TheatreController()
        
    def initialize(self):
        self.createMovies()
        self.createTheatre()
    
    def createTheatre(self):
        pass
    
    def createMovies(self):
        pass
    
    def createBooking(self, userCity: City, movieName: str):
        # get movie by City
        
        # get interested movie
        
        # get all shows of the interested movie in user City
        # select seats
        # check if seat is booked
        # if no create booking
        # update seat booking

bms = BookMyShow()



