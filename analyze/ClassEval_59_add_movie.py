import numpy as np
from datetime import datetime

def add_movie(self, name, price, start_time, end_time, n):
    """
    Add a new movie into self.movies
    :param name: str, movie name
    :param price: float, price for one ticket
    :param start_time: str
    :param end_time: str
    :param n: int, the size of seats(n*n)
    >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    >>> system.movies
    [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
    'seats': array([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])}]
    """
    # Parse start_time and end_time strings to datetime objects
    start_dt = datetime.strptime(start_time, '%H:%M').replace(year=1900, month=1, day=1)
    end_dt = datetime.strptime(end_time, '%H:%M').replace(year=1900, month=1, day=1)
    
    # Create n*n seats array initialized with zeros
    seats = np.zeros((n, n))
    
    # Create movie dictionary
    movie = {
        'name': name,
        'price': price,
        'start_time': start_dt,
        'end_time': end_dt,
        'seats': seats
    }
    
    # Add movie to self.movies list
    self.movies.append(movie)