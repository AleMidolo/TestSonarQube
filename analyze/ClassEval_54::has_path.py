def has_path(self, pos1, pos2):
    """
        Check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether there is a path between two icons
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
    if abs(x1 - x2) + abs(y1 - y2) == 1:
        return True
    visited = set()
    queue = deque()
    queue.append((x1, y1, 0, 0, 0))
    visited.add((x1, y1, 0, 0, 0))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, turns, dx, dy = queue.popleft()
        for ndx, ndy in directions:
            nx, ny = (x + ndx, y + ndy)
            if not (0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]):
                continue
            if (nx, ny) != (x2, y2) and self.board[nx][ny] != ' ':
                continue
            new_turns = turns
            if (dx, dy) != (0, 0) and (ndx, ndy) != (dx, dy):
                new_turns += 1
            if new_turns > 2:
                continue
            if (nx, ny) == (x2, y2):
                return True
            state = (nx, ny, new_turns, ndx, ndy)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False