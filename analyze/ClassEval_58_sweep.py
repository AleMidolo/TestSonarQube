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
    # Check if the position contains a mine
    if self.minesweeper_map[x][y] == 'X':
        return False
    
    # Reveal the cell
    self.player_map[x][y] = self.minesweeper_map[x][y]
    
    # If the cell is 0, recursively reveal adjacent cells
    if self.minesweeper_map[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Check bounds
                if 0 <= nx < len(self.minesweeper_map) and 0 <= ny < len(self.minesweeper_map[0]):
                    # Only sweep if not already revealed
                    if self.player_map[nx][ny] == '-':
                        self.sweep(nx, ny)
    
    # Check if the player has won (all non-mine cells revealed)
    for i in range(len(self.minesweeper_map)):
        for j in range(len(self.minesweeper_map[0])):
            if self.minesweeper_map[i][j] != 'X' and self.player_map[i][j] == '-':
                return self.player_map
    
    return True