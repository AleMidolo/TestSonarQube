def has_path(self, pos1, pos2):
    """
        verifica si hay un camino entre dos íconos
        :param pos1: tupla de posición (x, y) del primer ícono
        :param pos2: tupla de posición (x, y) del segundo ícono
        :return: True o False, representando si hay un camino entre dos íconos
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
    x1, y1 = pos1
    x2, y2 = pos2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    queue.append((x1, y1, 0, -1))
    visited.add((x1, y1, 0, -1))
    while queue:
        x, y, turns, dir_idx = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        for new_dir_idx, (dx, dy) in enumerate(directions):
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (x2, y2) and self.board[new_x][new_y] != ' ':
                continue
            new_turns = turns
            if dir_idx != -1 and new_dir_idx != dir_idx:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_turns, new_dir_idx)
            if state in visited:
                continue
            visited.add(state)
            queue.append(state)
    return False