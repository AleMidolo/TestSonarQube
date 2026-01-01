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
    start_state = tuple((tuple(row) for row in self.initial_state))
    goal_state = tuple((tuple(row) for row in self.goal_state))
    queue = deque()
    queue.append((start_state, []))
    visited = set()
    visited.add(start_state)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        current_state_list = [list(row) for row in current_state]
        possible_moves = self.get_possible_moves(current_state_list)
        for move in possible_moves:
            new_state_list = self.move(current_state_list, move)
            new_state = tuple((tuple(row) for row in new_state_list))
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move]))
    return None