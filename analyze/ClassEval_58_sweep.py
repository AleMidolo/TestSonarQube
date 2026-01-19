def sweep(self, x, y):
    """
    दिए गए स्थान को स्वीप करता है।
    :param x: स्थान का x समन्वय, int.
    :param y: स्थान का y समन्वय, int.
    :return: यदि खिलाड़ी ने खेल जीत लिया है तो True, अन्यथा False, यदि खेल अभी भी जारी है, तो खिलाड़ी का मानचित्र लौटाएं, list.
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
                if 0 <= nx < len(self.minesweeper_map) and 0 <= ny < len(self.minesweeper_map[0]):
                    if self.player_map[nx][ny] == '-':
                        self.sweep(nx, ny)
    
    # Check if the player has won (all non-mine cells revealed)
    for i in range(len(self.minesweeper_map)):
        for j in range(len(self.minesweeper_map[0])):
            if self.minesweeper_map[i][j] != 'X' and self.player_map[i][j] == '-':
                return self.player_map
    
    return True