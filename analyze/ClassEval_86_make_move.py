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
    # Check if the position is valid and empty
    if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
        if self.board[row][col] is None or self.board[row][col] == ' ' or self.board[row][col] == '':
            # Place the current player's mark
            self.board[row][col] = self.current_player
            # Switch to the other player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
    return False