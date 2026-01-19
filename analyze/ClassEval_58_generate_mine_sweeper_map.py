def generate_mine_sweeper_map(self):
    """
    Genera un mapa de buscaminas con el tamaño dado del tablero y el número de minas. El parámetro dado n es el tamaño del tablero, el tamaño del tablero es n*n, el parámetro k es el número de minas, 'X' representa la mina, otros números representan la cantidad de minas alrededor de la posición.
    :return: El mapa de buscaminas, lista.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_mine_sweeper_map()
    [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

    """
    import random
    
    # Initialize the board with zeros
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    # Place mines randomly
    mines_placed = 0
    while mines_placed < self.k:
        row = random.randint(0, self.n - 1)
        col = random.randint(0, self.n - 1)
        
        # Only place mine if position doesn't already have one
        if board[row][col] != 'X':
            board[row][col] = 'X'
            mines_placed += 1
    
    # Calculate numbers for non-mine cells
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] != 'X':
                # Count adjacent mines
                mine_count = 0
                # Check all 8 adjacent positions
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        # Check if position is within bounds
                        if 0 <= ni < self.n and 0 <= nj < self.n:
                            if board[ni][nj] == 'X':
                                mine_count += 1
                board[i][j] = mine_count
    
    return board