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
    def time_to_minutes(time_str):
        """Convert HH:MM format to minutes since midnight"""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)
    
    available = []
    
    # Iterate through all movies in the system
    for movie_name, movie_info in self.movies.items():
        movie_start = time_to_minutes(movie_info['start_time'])
        movie_end = time_to_minutes(movie_info['end_time'])
        
        # Check if movie's time range is within the specified time range
        if movie_start >= start_minutes and movie_end <= end_minutes:
            available.append(movie_name)
    
    return available