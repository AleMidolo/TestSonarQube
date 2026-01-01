def book_ticket(self, name, seats_to_book):
    """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """
    movie = None
    for m in self.movies:
        if m['name'] == name:
            movie = m
            break
    if movie is None:
        return 'Movie not found.'
    seats = movie['seats']
    n_rows, n_cols = seats.shape
    for row, col in seats_to_book:
        if row < 0 or row >= n_rows or col < 0 or (col >= n_cols):
            return 'Booking failed.'
        if seats[row, col] != 0:
            return 'Booking failed.'
    for row, col in seats_to_book:
        seats[row, col] = 1
    return 'Booking success.'