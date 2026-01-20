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
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    
    available = []
    
    for movie_name, movie_data in self.movies.items():
        movie_start = time_to_minutes(movie_data['start_time'])
        movie_end = time_to_minutes(movie_data['end_time'])
        
        # Check if movie's time range is within the specified range
        if movie_start >= start_minutes and movie_end <= end_minutes:
            available.append(movie_name)
    
    return available