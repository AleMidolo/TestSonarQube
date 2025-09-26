from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        movie = {
            'name': name,
            'price': price,
            'start_time': self._parse_time(start_time),
            'end_time': self._parse_time(end_time),
            'seats': self._initialize_seats(n)
        }
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        movie = self._find_movie_by_name(name)
        if not movie:
            return "Movie not found."
        
        return self._attempt_booking(movie, seats_to_book)

    def available_movies(self, start_time, end_time):
        start_time = self._parse_time(start_time)
        end_time = self._parse_time(end_time)

        return [movie['name'] for movie in self.movies if self._is_movie_available(movie, start_time, end_time)]

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, '%H:%M')

    def _initialize_seats(self, n):
        return np.zeros((n, n))

    def _find_movie_by_name(self, name):
        for movie in self.movies:
            if movie['name'] == name:
                return movie
        return None

    def _attempt_booking(self, movie, seats_to_book):
        for seat in seats_to_book:
            if movie['seats'][seat[0]][seat[1]] == 0:
                movie['seats'][seat[0]][seat[1]] = 1
            else:
                return "Booking failed."
        return "Booking success."

    def _is_movie_available(self, movie, start_time, end_time):
        return start_time <= movie['start_time'] and movie['end_time'] <= end_time