def check_winner(self):
    """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(self.board_size):
        for col in range(self.board_size):
            if self.board[row][col] != ' ':
                for direction in directions:
                    if self._check_five_in_a_row(row, col, direction):
                        return self.board[row][col]
    return None