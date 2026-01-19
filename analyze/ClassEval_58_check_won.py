def check_won(self, map):
    """
    Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
    :return: True if the player has won the game, False otherwise.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> minesweeper_game.check_won(minesweeper_game.player_map)
    False

    """
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '-':
                # Check if the corresponding cell in minesweeper_map is a mine
                if self.minesweeper_map[i][j] != 'X':
                    # There's an unrevealed cell that's not a mine
                    return False
    return True