def has_path(self, pos1, pos2):
    """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
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
    while queue:
        x, y, turns, dir_idx = queue.popleft()
        if (x, y) == (end_x, end_y):
            return True
        for new_dir_idx, (dx, dy) in enumerate(directions):
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (end_x, end_y) and self.board[new_x][new_y] != ' ':
                continue
            new_turns = turns
            if dir_idx != -1 and new_dir_idx != dir_idx:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_turns, new_dir_idx)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False