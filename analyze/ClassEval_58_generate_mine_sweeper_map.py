def generate_mine_sweeper_map(self):
    """
    Generates a minesweeper map with the given size of the board and the number of mines,the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
    :return: The minesweeper map, list.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_mine_sweeper_map()
    [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

    """
    import random
    
    # Initialize the board with zeros
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    # Randomly place k mines on the board
    positions = [(i, j) for i in range(self.n) for j in range(self.n)]
    mine_positions = random.sample(positions, self.k)
    
    # Place mines on the board
    for row, col in mine_positions:
        board[row][col] = 'X'
    
    # Calculate numbers for non-mine cells
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] != 'X':
                # Count adjacent mines
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.n and 0 <= nj < self.n:
                            if board[ni][nj] == 'X':
                                count += 1
                board[i][j] = count
    
    return board