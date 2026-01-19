def check_winner(self):
    """
    Controlla se c'è un vincitore cercando cinque in fila in tutte le direzioni (orizzontale, verticale, diagonale).
    return: il simbolo del giocatore vincente (o 'X' o 'O') se c'è un vincitore, altrimenti None.
    >>> gomokuGame = GomokuGame(10)
    >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
    >>> for move in moves:
    ...     gomokuGame.make_move(move[0], move[1])
    >>> gomokuGame.check_winner()
    'X'
    """
    # Definisce le quattro direzioni da controllare: orizzontale, verticale, e due diagonali
    directions = [
        (0, 1),   # orizzontale
        (1, 0),   # verticale
        (1, 1),   # diagonale principale
        (1, -1)   # diagonale secondaria
    ]
    
    # Itera su tutte le celle della griglia
    for row in range(self.size):
        for col in range(self.size):
            # Salta le celle vuote
            if self.board[row][col] is None:
                continue
            
            player = self.board[row][col]
            
            # Controlla in tutte e quattro le direzioni
            for dr, dc in directions:
                count = 1  # Conta la cella corrente
                
                # Controlla in avanti nella direzione
                r, c = row + dr, col + dc
                while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                    count += 1
                    r += dr
                    c += dc
                
                # Se abbiamo trovato 5 o più in fila, abbiamo un vincitore
                if count >= 5:
                    return player
    
    return None