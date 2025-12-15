class EightPuzzle: 
    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]

        if direction == 'up':
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down':
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left':
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right':
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

        return new_state

    def get_possible_moves(self, state):
        """
        根据当前状态，找到所有可能的移动方向。只有4个方向：'上'，'下'，'左'，'右'。
        :param state: 一个3*3大小的整数列表，存储当前状态。
        :return moves: 一个字符串列表，存储根据当前状态所有可能的移动方向。
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['上', '左', '右']
        """
        moves = []
        i, j = self.find_blank(state)

        if i > 0:  # Up
            moves.append('up')
        if i < 2:  # Down
            moves.append('down')
        if j > 0:  # Left
            moves.append('left')
        if j < 2:  # Right
            moves.append('right')

        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
        open_list = [(self.initial_state, [])]
        closed_list = []

        while open_list:
            current_state, path = open_list.pop(0)
            closed_list.append(current_state)

            if current_state == self.goal_state:
                return path

            for move in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move)
                if new_state not in closed_list:
                    open_list.append((new_state, path + [move]))

        return None