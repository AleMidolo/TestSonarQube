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
    x1, y1 = pos1
    x2, y2 = pos2
    for dx, dy in directions:
        nx, ny = (x1 + dx, y1 + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (x2, y2):
                return True
            if self.board[nx][ny] == ' ':
                queue.append((nx, ny, 0, (dx, dy)))
                visited.add((nx, ny, 0, (dx, dy)))
    queue.append((x1, y1, 0, (0, 0)))
    visited.add((x1, y1, 0, (0, 0)))
    while queue:
        x, y, turns, direction = queue.popleft()
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                if (nx, ny) == (x2, y2):
                    return True
                if self.board[nx][ny] == ' ':
                    new_turns = turns
                    if direction != (0, 0) and (dx, dy) != direction:
                        new_turns += 1
                    if new_turns <= 2:
                        state = (nx, ny, new_turns, (dx, dy))
                        if state not in visited:
                            visited.add(state)
                            queue.append(state)
    return False