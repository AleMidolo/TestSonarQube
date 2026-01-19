def available_movies(self, start_time, end_time):
    """
    Ottieni un elenco di film disponibili all'interno dell'intervallo di tempo specificato
    :param start_time: str, ora di inizio nel formato HH:MM
    :param end_time: str, ora di fine nel formato HH:MM
    :return: lista di str, nomi dei film disponibili
    >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    >>> system.available_movies('12:00', '22:00')
    ['Batman']
    """
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    available_movies = []

    for movie in self.movies:
        if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
            available_movies.append(movie['name'])

    return available_movies