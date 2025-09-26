from datetime import datetime
import numpy as np

class Movie:
    def __init__(self, name, price, start_time, end_time, n):
        self.name = name
        self.price = price
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.end_time = datetime.strptime(end_time, '%H:%M')
        self.seats = np.zeros((n, n))

    def book_seat(self, seat):
        if self.seats[seat[0]][seat[1]] == 0:
            self.seats[seat[0]][seat[1]] = 1
            return True
        return False

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        movie = Movie(name, price, start_time, end_time, n)
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        movie = self.find_movie(name)
        if not movie:
            return "Movie not found."
        
        for seat in seats_to_book:
            if not movie.book_seat(seat):
                return "Booking failed."
        return "Booking success."

    def available_movies(self, start_time, end_time):
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        return [movie.name for movie in self.movies if self.is_movie_available(movie, start_time, end_time)]

    def find_movie(self, name):
        for movie in self.movies:
            if movie.name == name:
                return movie
        return None

    def is_movie_available(self, movie, start_time, end_time):
        return start_time <= movie.start_time and movie.end_time <= end_time