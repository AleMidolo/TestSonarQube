def generate_mine_sweeper_map(self):
    """
        Genera una mappa di campo minato con la dimensione data della griglia e il numero di mine, il parametro dato n è la dimensione della griglia, la dimensione della griglia è n*n, il parametro k è il numero di mine, 'X' rappresenta la mina, altri numeri rappresentano il numero di mine attorno alla posizione.
        :return: La mappa del campo minato, lista.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    mines_placed = 0
    while mines_placed < self.k:
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        if board[x][y] != 'X':
            board[x][y] = 'X'
            mines_placed += 1
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] == 'X':
                continue
            mine_count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = (i + dx, j + dy)
                    if 0 <= nx < self.n and 0 <= ny < self.n:
                        if board[nx][ny] == 'X':
                            mine_count += 1
            board[i][j] = mine_count
    return board