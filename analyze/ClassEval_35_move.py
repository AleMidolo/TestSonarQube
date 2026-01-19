def move(self, state, direction):
    """
    找到空白块，然后使棋盘向给定方向移动。
    :param state: 一个 3*3 大小的整数列表，存储移动前的状态。
    :param direction: str，只有 4 个方向 'up', 'down', 'left', 'right'
    :return new_state: 一个 3*3 大小的整数列表，存储移动后的状态。
    >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
    [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
    """
    # 创建状态的深拷贝
    new_state = [row[:] for row in state]
    
    # 找到空白块（0）的位置
    zero_row, zero_col = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
    
    # 根据方向移动空白块
    if direction == 'up':
        # 空白块向上移动，即与上方的块交换
        if zero_row > 0:
            new_state[zero_row][zero_col] = new_state[zero_row - 1][zero_col]
            new_state[zero_row - 1][zero_col] = 0
    elif direction == 'down':
        # 空白块向下移动，即与下方的块交换
        if zero_row < 2:
            new_state[zero_row][zero_col] = new_state[zero_row + 1][zero_col]
            new_state[zero_row + 1][zero_col] = 0
    elif direction == 'left':
        # 空白块向左移动，即与左边的块交换
        if zero_col > 0:
            new_state[zero_row][zero_col] = new_state[zero_row][zero_col - 1]
            new_state[zero_row][zero_col - 1] = 0
    elif direction == 'right':
        # 空白块向右移动，即与右边的块交换
        if zero_col < 2:
            new_state[zero_row][zero_col] = new_state[zero_row][zero_col + 1]
            new_state[zero_row][zero_col + 1] = 0
    
    return new_state