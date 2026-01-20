def check_winner(self):
    """
    Verifica si hay un ganador buscando cinco en fila en todas las direcciones (horizontal, vertical, diagonal).
    return: el símbolo del jugador ganador (ya sea 'X' o 'O') si hay un ganador, o None en caso contrario.
    >>> gomokuGame = GomokuGame(10)
    >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
    >>> for move in moves:
    ...     gomokuGame.make_move(move[0], move[1])
    >>> gomokuGame.check_winner()
    'X'
    """
    # Direcciones: horizontal, vertical, diagonal (\), diagonal (/)
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal \
        (1, -1)   # diagonal /
    ]
    
    # Recorrer cada posición del tablero
    for row in range(self.size):
        for col in range(self.size):
            # Si la celda está vacía, continuar
            if self.board[row][col] is None:
                continue
            
            player = self.board[row][col]
            
            # Verificar en cada dirección
            for dr, dc in directions:
                count = 1  # Contar la pieza actual
                
                # Contar en la dirección positiva
                r, c = row + dr, col + dc
                while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                    count += 1
                    r += dr
                    c += dc
                
                # Contar en la dirección negativa
                r, c = row - dr, col - dc
                while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                    count += 1
                    r -= dr
                    c -= dc
                
                # Si hay 5 o más en fila, hay un ganador
                if count >= 5:
                    return player
    
    return None