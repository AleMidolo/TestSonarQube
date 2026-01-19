def generate_mine_sweeper_map(self):
    """
        Generates a minesweeper map with the given size of the board and the number of mines,the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
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
    for i in range(self.n):
        for j in range(self.n):
            if arr[i][j] == 0:
                arr[i][j] = 0
            elif arr[i][j] != 'X':
                arr[i][j] = str(arr[i][j])
    return arr