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
    from collections import deque
    open_list = deque([(self.initial_state, [])])
    visited = set()
    visited.add(tuple(map(tuple, self.initial_state)))
    while open_list:
        current_state, path = open_list.popleft()
        if current_state == self.goal_state:
            return path
        for move_direction in self.get_possible_moves(current_state):
            new_state = self.move(current_state, move_direction)
            new_state_tuple = tuple(map(tuple, new_state))
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                open_list.append((new_state, path + [move_direction]))
    return []