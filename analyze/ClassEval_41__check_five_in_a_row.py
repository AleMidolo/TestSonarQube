def _check_five_in_a_row(self, row, col, direction):
    """
        checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell,
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy repectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
        True
        >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
        False
        """
    dx, dy = direction
    symbol = self.board[row][col]
    count = 1
    r, c = (row + dx, col + dy)
    while 0 <= r < self.board_size and 0 <= c < self.board_size and (self.board[r][c] == symbol):
        count += 1
        if count >= 5:
            return True
        r += dx
        c += dy
    r, c = (row - dx, col - dy)
    while 0 <= r < self.board_size and 0 <= c < self.board_size and (self.board[r][c] == symbol):
        count += 1
        if count >= 5:
            return True
        r -= dx
        c -= dy
    return count >= 5