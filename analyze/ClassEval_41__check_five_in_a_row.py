def _check_five_in_a_row(self, row, col, direction):
    """
    verifica si hay cinco símbolos consecutivos del mismo jugador en una fila comenzando desde una celda dada en una dirección dada (horizontal, vertical, diagonal).
    Cuenta el número de símbolos consecutivos en esa dirección comenzando desde la celda dada,
    :param row: int, fila de la celda dada
    :param col: int, columna de la celda dada
    :param direction: tuple, (int, int), nombrado como (dx, dy). La fila y la columna se incrementarán en varios dx y dy respectivamente.
    :return: True si hay cinco símbolos consecutivos del mismo jugador, y False en caso contrario.
    >>> gomokuGame = GomokuGame(10)
    >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
    >>> for move in moves:
    ...     gomokuGame.make_move(move[0], move[1])
    >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
    True
    >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
    False
    """
    # Get the player symbol at the starting position
    player = self.board[row][col]
    
    # If the cell is empty, there can't be five in a row
    if player is None or player == 0 or player == '':
        return False
    
    dx, dy = direction
    count = 1  # Count the starting cell
    
    # Check in the positive direction
    current_row = row + dx
    current_col = col + dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row += dx
        current_col += dy
    
    # Check in the negative direction
    current_row = row - dx
    current_col = col - dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row -= dx
        current_col -= dy
    
    return count >= 5