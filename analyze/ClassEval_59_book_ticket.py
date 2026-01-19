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
    # Check if movie exists
    if name not in self.movies:
        return "Movie not found."
    
    # Get the seats grid for this movie
    seats = self.movies[name]['seats']
    
    # Check if all requested seats are available (value is 0)
    for row, col in seats_to_book:
        # Check if seat coordinates are valid
        if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
            return "Booking failed."
        # Check if seat is already booked
        if seats[row][col] != 0:
            return "Booking failed."
    
    # All seats are available, book them (set to 1)
    for row, col in seats_to_book:
        seats[row][col] = 1
    
    return "Booking success."