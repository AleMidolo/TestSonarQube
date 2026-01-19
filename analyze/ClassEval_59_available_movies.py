def available_movies(self, start_time, end_time):
    """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    available = []
    for movie in self.movies:
        if movie['start_time'] <= end and movie['end_time'] >= start:
            available.append(movie['name'])
    return available