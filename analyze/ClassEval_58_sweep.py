def sweep(self, x, y):
    """
    Scopre la posizione data.
    :param x: La coordinata x della posizione, int.
    :param y: La coordinata y della posizione, int.
    :return: True se il giocatore ha vinto il gioco, False altrimenti; se il gioco continua, restituisce la mappa del giocatore, list.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> minesweeper_game.sweep(1, 1)
    [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]

    """
    # Se la posizione contiene una mina, il giocatore perde
    if self.minesweeper_map[x][y] == 'X':
        return False
    
    # Scopre la posizione
    self.player_map[x][y] = self.minesweeper_map[x][y]
    
    # Se la posizione è 0, scopre ricorsivamente le posizioni adiacenti
    if self.minesweeper_map[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.minesweeper_map) and 0 <= ny < len(self.minesweeper_map[0]):
                    if self.player_map[nx][ny] == '-':
                        self.sweep(nx, ny)
    
    # Controlla se il giocatore ha vinto
    for i in range(len(self.player_map)):
        for j in range(len(self.player_map[0])):
            if self.player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                return self.player_map
    
    return True