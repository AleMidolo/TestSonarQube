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
        """Convierte una hora en formato HH:MM a minutos desde medianoche"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    
    available = []
    
    # Asumiendo que self.movies es un diccionario o lista que contiene las películas
    # con información sobre su horario de inicio y fin
    if hasattr(self, 'movies'):
        for movie_name, movie_info in self.movies.items():
            movie_start = time_to_minutes(movie_info['start_time'])
            movie_end = time_to_minutes(movie_info['end_time'])
            
            # La película está disponible si su horario está completamente dentro del rango
            if start_minutes <= movie_start and movie_end <= end_minutes:
                available.append(movie_name)
    
    return available