import numpy as np
from datetime import datetime

def add_movie(self, name, price, start_time, end_time, n):
    """
    将新电影添加到 self.movies
    :param name: str, 电影名称
    :param price: float, 一张票的价格
    :param start_time: str
    :param end_time: str
    :param n: int, 座位的大小(n*n)
    >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    >>> system.movies
    [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
    'seats': array([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])}]
    """
    # Parse time strings to datetime objects
    start_dt = datetime.strptime(start_time, '%H:%M').replace(year=1900, month=1, day=1)
    end_dt = datetime.strptime(end_time, '%H:%M').replace(year=1900, month=1, day=1)
    
    # Create n x n seats array initialized with zeros
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