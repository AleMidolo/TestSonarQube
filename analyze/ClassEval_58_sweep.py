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
    # Si la posición contiene una mina, el jugador pierde
    if self.minesweeper_map[x][y] == 'X':
        return False
    
    # Revelar la celda actual
    self.player_map[x][y] = self.minesweeper_map[x][y]
    
    # Si la celda es 0, revelar recursivamente las celdas adyacentes
    if self.minesweeper_map[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Verificar límites
                if 0 <= nx < len(self.minesweeper_map) and 0 <= ny < len(self.minesweeper_map[0]):
                    # Solo revelar si aún no ha sido revelada
                    if self.player_map[nx][ny] == '-':
                        self.sweep(nx, ny)
    
    # Verificar si el jugador ha ganado (todas las celdas sin minas reveladas)
    for i in range(len(self.minesweeper_map)):
        for j in range(len(self.minesweeper_map[0])):
            if self.minesweeper_map[i][j] != 'X' and self.player_map[i][j] == '-':
                # Aún hay celdas sin revelar que no son minas
                return self.player_map
    
    # Todas las celdas sin minas han sido reveladas
    return True