def generate_mine_sweeper_map(self):
    """
        Genera un mapa de buscaminas con el tamaño dado del tablero y el número de minas. El parámetro dado n es el tamaño del tablero, el tamaño del tablero es n*n, el parámetro k es el número de minas, 'X' representa la mina, otros números representan la cantidad de minas alrededor de la posición.
        :return: El mapa de buscaminas, lista.
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
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < self.n and 0 <= ny < self.n and (board[nx][ny] != 'X'):
                        board[nx][ny] += 1
    return board