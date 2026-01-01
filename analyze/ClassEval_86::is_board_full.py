def is_board_full(self):
    """
        जांचें कि खेल का बोर्ड पूरी तरह से भरा हुआ है या नहीं।
        :return: bool, यह दर्शाता है कि खेल का बोर्ड भरा हुआ है या नहीं
        >>> ttt.is_board_full()
        False
        """
    return all((cell != ' ' for row in self.board for cell in row))