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
    for movie in self.movies:
        if movie['name'].lower() == name.lower():
            for seat in seats_to_book:
                row, col = seat
                if movie['seats'][row, col] == 0:
                    movie['seats'][row, col] = 1
                else:
                    return 'Booking failed.'
            return 'Booking success.'
    return 'Movie not found.'