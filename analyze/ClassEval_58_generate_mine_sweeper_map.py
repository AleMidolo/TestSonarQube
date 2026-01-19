def generate_mine_sweeper_map(self):
    """
        Genera un mapa de buscaminas con el tamaño dado del tablero y el número de minas. El parámetro dado n es el tamaño del tablero, el tamaño del tablero es n*n, el parámetro k es el número de minas, 'X' representa la mina, otros números representan la cantidad de minas alrededor de la posición.
        :return: El mapa de buscaminas, lista.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
    minesweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
    mines_placed = 0
    while mines_placed < self.k:
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        if minesweeper_map[x][y] != 'X':
            minesweeper_map[x][y] = 'X'
            mines_placed += 1
            for i in range(max(0, x - 1), min(self.n, x + 2)):
                for j in range(max(0, y - 1), min(self.n, y + 2)):
                    if minesweeper_map[i][j] != 'X':
                        minesweeper_map[i][j] += 1
    return minesweeper_map