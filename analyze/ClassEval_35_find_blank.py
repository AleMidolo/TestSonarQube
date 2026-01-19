def find_blank(self, state):
    """
        找到当前状态的空白位置，即0元素。
        :param state: 一个3*3大小的整数列表，存储当前状态。
        :return i, j: 两个整数，表示空白块的坐标。
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)