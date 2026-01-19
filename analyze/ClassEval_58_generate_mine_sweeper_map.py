def generate_mine_sweeper_map(self):
    """
    Genera una mappa di campo minato con la dimensione data della griglia e il numero di mine, il parametro dato n è la dimensione della griglia, la dimensione della griglia è n*n, il parametro k è il numero di mine, 'X' rappresenta la mina, altri numeri rappresentano il numero di mine attorno alla posizione.
    :return: La mappa del campo minato, lista.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_mine_sweeper_map()
    [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

    """
    import random
    
    # Initialize the grid with zeros
    grid = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    # Randomly place k mines
    positions = [(i, j) for i in range(self.n) for j in range(self.n)]
    mine_positions = random.sample(positions, self.k)
    
    # Place mines on the grid
    for row, col in mine_positions:
        grid[row][col] = 'X'
    
    # Calculate numbers for non-mine cells
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(self.n):
        for j in range(self.n):
            if grid[i][j] != 'X':
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.n and 0 <= nj < self.n and grid[ni][nj] == 'X':
                        mine_count += 1
                grid[i][j] = mine_count
    
    return grid