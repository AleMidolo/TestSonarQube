def is_game_over(self):
        """
        check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False, indicating whether the game is over
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
        for row in self.board:
            if any(icon != ' ' for icon in row):
                return False
        return True