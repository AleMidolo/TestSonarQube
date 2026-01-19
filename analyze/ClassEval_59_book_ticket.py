def book_ticket(self, name, seats_to_book):
    """
    预订电影票。如果成功预订，则在self.movies中更改座位值。
    :param name: str, 电影名称
    :param seats_to_book: 元组列表, 表示要预订的座位 [(row1, col1), (row2, col2), ...]
    :return: str, 预订状态消息。 "Movie not found." 表示没有该电影。
            "Booking success." 表示成功预订，或 "Booking failed." 表示其他情况
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
    
    # Get the movie's seating arrangement
    seats = self.movies[name]['seats']
    
    # First, check if all requested seats are available (value is 0)
    for row, col in seats_to_book:
        # Check if seat coordinates are valid
        if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
            return "Booking failed."
        # Check if seat is already booked (value is 1)
        if seats[row][col] == 1:
            return "Booking failed."
    
    # If all seats are available, book them (set value to 1)
    for row, col in seats_to_book:
        seats[row][col] = 1
    
    return "Booking success."