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
    for movie in self.movies:
        if movie['name'].lower() == name.lower():
            for seat in seats_to_book:
                row, col = seat
                if movie['seats'][row][col] == 0:
                    movie['seats'][row][col] = 1
                else:
                    return 'बुकिंग विफल।'
            return 'बुकिंग सफल।'
    return 'फिल्म नहीं मिली।'