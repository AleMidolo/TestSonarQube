def has_path(self, pos1, pos2):
    """
        检查两个图标之间是否存在路径
        :param pos1: 第一个图标的位置元组(x, y)
        :param pos2: 第二个图标的位置元组(x, y)
        :return: True 或 False，表示两个图标之间是否存在路径
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    start_x, start_y = pos1
    end_x, end_y = pos2
    for i, (dx, dy) in enumerate(directions):
        queue.append((start_x, start_y, 0, i))
        visited.add((start_x, start_y, 0, i))
    queue.append((start_x, start_y, 0, -1))
    visited.add((start_x, start_y, 0, -1))
    while queue:
        x, y, turns, direction = queue.popleft()
        if (x, y) == (end_x, end_y):
            return True
        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (end_x, end_y) and self.board[new_x][new_y] != ' ':
                continue
            new_turns = turns
            if direction != -1 and i != direction:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_turns, i)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False