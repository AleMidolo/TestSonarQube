def is_game_over(self):
    """
        जांचें कि क्या खेल समाप्त हो गया है (यानी, यदि खेल बोर्ड पर और कोई आइकन नहीं हैं)
        :return: True या False, जो दर्शाता है कि क्या खेल समाप्त हो गया है
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
    for row in self.board:
        for cell in row:
            if cell != ' ':
                return False
    return True