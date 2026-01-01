def available_movies(self, start_time, end_time):
    """
        Obtiene una lista de películas disponibles dentro del rango de tiempo especificado
        :param start_time: str, hora de inicio en formato HH:MM
        :param end_time: str, hora de fin en formato HH:MM
        :return: lista de str, nombres de las películas disponibles
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
    available = []
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    for movie in self.movies:
        if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
            available.append(movie['name'])
    return available