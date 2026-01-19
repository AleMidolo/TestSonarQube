def solve(self):
    """
        使用 BFS 算法找到从初始状态到目标状态的路径解决方案。
        维护一个名为 open_list 的列表作为队列，并将初始状态添加到该队列中。
        始终访问并弹出索引为 0 的元素，调用 get_possible_moves 方法查找所有可能的方向。
        遍历 possible_moves 列表并调用 move 方法以获取多个新状态，然后将它们添加到队列中。
        重复上述步骤，直到 open_list 为空或状态已更改为目标状态。
        :return path: list of str，目标状态的解决方案。
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
        possible_moves = self.get_possible_moves(current_state)
        for move_direction in possible_moves:
            new_state = self.move(current_state, move_direction)
            new_path = path + [move_direction]
            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                open_list.append((new_state, new_path))
    return []