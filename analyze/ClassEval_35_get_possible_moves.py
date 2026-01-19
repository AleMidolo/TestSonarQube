def get_possible_moves(self, state):
    """
    根据当前状态，找到所有可能的移动方向。只有4个方向：'上'，'下'，'左'，'右'。
    :param state: 一个3*3大小的整数列表，存储当前状态。
    :return moves: 一个字符串列表，存储根据当前状态所有可能的移动方向。
    >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
    ['上', '左', '右']
    """
    # 找到空格(0)的位置
    zero_row, zero_col = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break
    
    moves = []
    
    # 上：空格向上移动，即下面的数字向上移动到空格位置
    # 只有当空格不在第一行时才能向上移动
    if zero_row > 0:
        moves.append('上')
    
    # 下：空格向下移动，即上面的数字向下移动到空格位置
    # 只有当空格不在最后一行时才能向下移动
    if zero_row < 2:
        moves.append('下')
    
    # 左：空格向左移动，即右边的数字向左移动到空格位置
    # 只有当空格不在第一列时才能向左移动
    if zero_col > 0:
        moves.append('左')
    
    # 右：空格向右移动，即左边的数字向右移动到空格位置
    # 只有当空格不在最后一列时才能向右移动
    if zero_col < 2:
        moves.append('右')
    
    return moves