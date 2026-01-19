def make_move(self, row, col):
    """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
    if row < 0 or row >= 3 or col < 0 or (col >= 3):
        return False
    if self.board[row][col] != ' ':
        return False
    self.board[row][col] = self.current_player
    self.current_player = 'O' if self.current_player == 'X' else 'X'
    return True