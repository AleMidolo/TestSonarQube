def has_path(self, pos1, pos2):
    """
        Check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether there is a path between the two icons
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
    rows, cols = (self.BOARD_SIZE[0], self.BOARD_SIZE[1])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited[x1][y1] = True
    for dx, dy in directions:
        nx, ny = (x1 + dx, y1 + dy)
        if 0 <= nx < rows and 0 <= ny < cols and (self.board[nx][ny] == ' '):
            queue.append((nx, ny, 0, (dx, dy)))
            visited[nx][ny] = True
    while queue:
        x, y, turns, dir = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        if turns >= 2:
            continue
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols:
                if (self.board[nx][ny] == ' ' or (nx, ny) == (x2, y2)) and (not visited[nx][ny]):
                    new_turns = turns
                    if (dx, dy) != dir:
                        new_turns += 1
                    if new_turns <= 2:
                        queue.append((nx, ny, new_turns, (dx, dy)))
                        visited[nx][ny] = True
    return False