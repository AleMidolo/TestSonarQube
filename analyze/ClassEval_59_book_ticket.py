def book_ticket(self, name, seats_to_book):
    """
    एक फिल्म के लिए टिकट बुक करें। यदि सफलतापूर्वक बुक किया गया हो तो self.movies में सीटों का मान बदलें।
    :param name: str, फिल्म का नाम
    :param seats_to_book: टपल की सूची, बुक करने के लिए सीटों का प्रतिनिधित्व करती है [(row1, col1), (row2, col2), ...]
    :return: str, बुकिंग स्थिति संदेश। "फिल्म नहीं मिली।" यदि ऐसी कोई फिल्म नहीं है।
            "बुकिंग सफल।" यदि सफलतापूर्वक बुक किया गया, या "बुकिंग विफल।" अन्यथा
    >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
    'बुकिंग सफल।'
    >>> system.book_ticket('Batman', [(0, 0)])
    'बुकिंग विफल।'
    >>> system.book_ticket('batman', [(0, 0)])
    'फिल्म नहीं मिली।'
    """
    # Check if movie exists
    if name not in self.movies:
        return "फिल्म नहीं मिली।"
    
    movie = self.movies[name]
    seats = movie['seats']
    
    # Check if all seats are available (value is 0)
    for row, col in seats_to_book:
        # Check if indices are valid
        if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
            return "बुकिंग विफल।"
        # Check if seat is already booked (value is 1)
        if seats[row][col] == 1:
            return "बुकिंग विफल।"
    
    # All seats are available, book them
    for row, col in seats_to_book:
        seats[row][col] = 1
    
    return "बुकिंग सफल।"