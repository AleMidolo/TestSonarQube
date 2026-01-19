def check_won(self, map):
    """
        जांचता है कि क्या खिलाड़ी ने खेल जीत लिया है, यदि खिलाड़ी के मानचित्र में केवल खदानें हैं, तो True लौटाता है, अन्यथा False लौटाता है।
        :return: यदि खिलाड़ी ने खेल जीत लिया है तो True, अन्यथा False।
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
    for i in range(self.n):
        for j in range(self.n):
            if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                return False
    return True