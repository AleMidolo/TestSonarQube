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
    # Get the symbol at the starting position
    symbol = self.board[row][col]
    
    # If the cell is empty, there can't be five in a row
    if symbol is None or symbol == 0 or symbol == '':
        return False
    
    dx, dy = direction
    count = 1  # Count the starting cell
    
    # Check in the positive direction
    current_row, current_col = row + dx, col + dy
    while (0 <= current_row < self.size and 
           0 <= current_col < self.size and 
           self.board[current_row][current_col] == symbol):
        count += 1
        current_row += dx
        current_col += dy
    
    # Check in the negative direction
    current_row, current_col = row - dx, col - dy
    while (0 <= current_row < self.size and 
           0 <= current_col < self.size and 
           self.board[current_row][current_col] == symbol):
        count += 1
        current_row -= dx
        current_col -= dy
    
    return count >= 5