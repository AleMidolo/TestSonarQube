class MinesweeperGame: 
    def __init__(self, n, k) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: The size of the board, int.
        :param k: The number of mines, int.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0


    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines,the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
    
        """
    
        arr = [[0 for row in range(self.n)] for column in range(self.n)]
        for num in range(self.k):
            x = random.randint(0, self.n-1)
            y = random.randint(0, self.n-1)
            arr[y][x] = 'X'
            if (x >= 0 and x <= self.n-2) and (y >= 0 and y <= self.n-1):
                if arr[y][x+1] != 'X':
                    arr[y][x+1] += 1
            if (x >= 1 and x <= self.n-1) and (y >= 0 and y <= self.n-1):
                if arr[y][x-1] != 'X':
                    arr[y][x-1] += 1
            if (x >= 1 and x <= self.n-1) and (y >= 1 and y <= self.n-1):
                if arr[y-1][x-1] != 'X':
                    arr[y-1][x-1] += 1
    
            if (x >= 0 and x <= self.n-2) and (y >= 1 and y <= self.n-1):
                if arr[y-1][x+1] != 'X':
                    arr[y-1][x+1] += 1
            if (x >= 0 and x <= self.n-1) and (y >= 1 and y <= self.n-1):
                if arr[y-1][x] != 'X':
                    arr[y-1][x] += 1
    
            if (x >= 0 and x <= self.n-2) and (y >= 0 and y <= self.n-2):
                if arr[y+1][x+1] != 'X':
                    arr[y+1][x+1] += 1
            if (x >= 1 and x <= self.n-1) and (y >= 0 and y <= self.n-2):
                if arr[y+1][x-1] != 'X':
                    arr[y+1][x-1] += 1
            if (x >= 0 and x <= self.n-1) and (y >= 0 and y <= self.n-2):
                if arr[y+1][x] != 'X':
                    arr[y+1][x] += 1
        return arr
    
    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_playerMap()
        [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    
        """
    
        arr = [['-' for row in range(self.n)] for column in range(self.n)]
        return arr
    
    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
    
        """
    
    
        if (self.minesweeper_map[x][y] == 'X'):
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            self.score += 1
            if self.check_won(self.player_map) == True:
                return True
            return self.player_map
    
    def check_won(self, map):
        """
        Controlla se il giocatore ha vinto il gioco; se ci sono solo mine nella mappa del giocatore, restituisce True, altrimenti restituisce False.
        :return: True se il giocatore ha vinto il gioco, False altrimenti.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
        for row in map:
            for cell in row:
                if cell == '-':
                    return False
        return True