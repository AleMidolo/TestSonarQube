def add_movie(self, name, price, start_time, end_time, n):
    """
        self.movies में एक नई फिल्म जोड़ें
        :param name: str, फिल्म का नाम
        :param price: float, एक टिकट की कीमत
        :param start_time: str
        :param end_time: str
        :param n: int, सीटों का आकार(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
    start_dt = datetime.strptime(start_time, '%H:%M').replace(year=1900, month=1, day=1)
    end_dt = datetime.strptime(end_time, '%H:%M').replace(year=1900, month=1, day=1)
    seats = np.zeros((n, n), dtype=float)
    movie = {'name': name, 'price': float(price), 'start_time': start_dt, 'end_time': end_dt, 'seats': seats}
    self.movies.append(movie)