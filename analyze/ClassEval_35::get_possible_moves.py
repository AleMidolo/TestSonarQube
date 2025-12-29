def get_possible_moves(self, state):
    """
        根据当前状态，找到所有可能的移动方向。只有4个方向：'上'，'下'，'左'，'右'。
        :param state: 一个3*3大小的整数列表，存储当前状态。
        :return moves: 一个字符串列表，存储根据当前状态所有可能的移动方向。
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['上', '左', '右']
        """
    i, j = self.find_blank(state)
    moves = []
    if i > 0:
        moves.append('up')
    if i < 2:
        moves.append('down')
    if j > 0:
        moves.append('left')
    if j < 2:
        moves.append('right')
    return moves