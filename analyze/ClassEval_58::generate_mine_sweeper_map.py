def generate_mine_sweeper_map(self):
    """
        Genera una mappa di campo minato con la dimensione data della griglia e il numero di mine, il parametro dato n è la dimensione della griglia, la dimensione della griglia è n*n, il parametro k è il numero di mine, 'X' rappresenta la mina, altri numeri rappresentano il numero di mine attorno alla posizione.
        :return: La mappa del campo minato, lista.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
    arr = [[0 for row in range(self.n)] for column in range(self.n)]
    mines_placed = 0
    while mines_placed < self.k:
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        if arr[x][y] != 'X':
            arr[x][y] = 'X'
            mines_placed += 1
            for i in range(max(0, x - 1), min(self.n, x + 2)):
                for j in range(max(0, y - 1), min(self.n, y + 2)):
                    if arr[i][j] != 'X':
                        arr[i][j] += 1
    return arr