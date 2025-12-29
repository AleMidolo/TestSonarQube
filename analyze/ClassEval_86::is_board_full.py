def is_board_full(self):
    """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
    for row in self.board:
        if ' ' in row:
            return False
    return True