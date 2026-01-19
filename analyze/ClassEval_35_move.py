def move(self, state, direction):
    """
    找到空白块，然后使棋盘向给定方向移动。
    :param state: 一个 3*3 大小的整数列表，存储移动前的状态。
    :param direction: str，只有 4 个方向 'up', 'down', 'left', 'right'
    :return new_state: 一个 3*3 大小的整数列表，存储移动后的状态。
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    i, j = self.find_blank(state)
    new_state = [row[:] for row in state]
    if direction == 'up':
        new_state[i][j], new_state[i - 1][j] = (new_state[i - 1][j], new_state[i][j])
    elif direction == 'down':
        new_state[i][j], new_state[i + 1][j] = (new_state[i + 1][j], new_state[i][j])
    elif direction == 'left':
        new_state[i][j], new_state[i][j - 1] = (new_state[i][j - 1], new_state[i][j])
    elif direction == 'right':
        new_state[i][j], new_state[i][j + 1] = (new_state[i][j + 1], new_state[i][j])
    return new_state