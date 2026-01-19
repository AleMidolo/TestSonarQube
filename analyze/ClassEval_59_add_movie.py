def add_movie(self, name, price, start_time, end_time, n):
    """
        Agrega una nueva película a self.movies
        :param name: str, nombre de la película
        :param price: float, precio de un boleto
        :param start_time: str
        :param end_time: str
        :param n: int, el tamaño de los asientos(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
    start_dt = datetime.strptime(start_time, '%H:%M')
    end_dt = datetime.strptime(end_time, '%H:%M')
    movie = {'name': name, 'price': price, 'start_time': start_dt, 'end_time': end_dt, 'seats': np.zeros((n, n))}
    self.movies.append(movie)