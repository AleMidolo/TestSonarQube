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
    movie = None
    for m in self.movies:
        if m['name'] == name:
            movie = m
            break
    if movie is None:
        return 'Movie not found.'
    n = movie['seats'].shape[0]
    for row, col in seats_to_book:
        if row < 0 or row >= n or col < 0 or (col >= n):
            return 'Booking failed.'
        if movie['seats'][row, col] != 0:
            return 'Booking failed.'
    for row, col in seats_to_book:
        movie['seats'][row, col] = 1
    return 'Booking success.'