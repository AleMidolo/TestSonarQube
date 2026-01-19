def is_board_full(self):
    """
    जांचें कि खेल का बोर्ड पूरी तरह से भरा हुआ है या नहीं।
    :return: bool, यह दर्शाता है कि खेल का बोर्ड भरा हुआ है या नहीं
    >>> ttt.is_board_full()
    False
    """
    for row in self.board:
        for cell in row:
            if cell is None or cell == '' or cell == ' ':
                return False
    return True