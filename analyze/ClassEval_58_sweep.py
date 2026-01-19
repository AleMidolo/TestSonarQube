def sweep(self, x, y):
    """
        Barre la posición dada.
        :param x: La coordenada x de la posición, int.
        :param y: La coordenada y de la posición, int.
        :return: True si el jugador ha ganado el juego, False en caso contrario, si el juego continúa, devuelve el mapa del jugador, lista.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]

        """
    if x < 0 or x >= self.n or y < 0 or (y >= self.n):
        return self.player_map
    if self.player_map[y][x] != '-':
        return self.player_map
    if self.minesweeper_map[y][x] == 'X':
        self.player_map[y][x] = 'X'
        return False
    self.player_map[y][x] = self.minesweeper_map[y][x]
    if self.minesweeper_map[y][x] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = (x + dx, y + dy)
                if 0 <= new_x < self.n and 0 <= new_y < self.n:
                    if self.player_map[new_y][new_x] == '-':
                        self.sweep(new_x, new_y)
    if self.check_won(self.player_map):
        return True
    return self.player_map