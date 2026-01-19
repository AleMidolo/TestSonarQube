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
    if self.initial_state == self.goal_state:
        return []
    queue = deque()
    queue.append((self.initial_state, []))
    visited = set()
    visited.add(tuple((tuple(row) for row in self.initial_state)))
    while queue:
        current_state, path = queue.popleft()
        if current_state == self.goal_state:
            return path
        possible_moves = self.get_possible_moves(current_state)
        for direction in possible_moves:
            new_state = self.move(current_state, direction)
            state_tuple = tuple((tuple(row) for row in new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((new_state, path + [direction]))
    return None