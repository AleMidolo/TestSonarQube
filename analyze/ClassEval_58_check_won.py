def check_won(self, map):
    """
    检查玩家是否赢得了游戏，如果玩家地图上只有地雷，则返回 True，否则返回 False。
    :return: 如果玩家赢得了游戏，则返回 True，否则返回 False。
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> minesweeper_game.check_won(minesweeper_game.player_map)
    False

    """
    for i in range(len(map)):
        for j in range(len(map[i])):
            # 如果玩家地图上还有未揭开的格子（'-'），检查对应位置是否是地雷
            if map[i][j] == '-':
                # 如果未揭开的位置不是地雷，则游戏未赢
                if self.minesweeper_map[i][j] != 'X':
                    return False
    # 所有未揭开的位置都是地雷，玩家赢得游戏
    return True