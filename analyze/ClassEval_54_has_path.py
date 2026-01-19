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
    for dx, dy in directions:
        nx, ny = (start_x + dx, start_y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if self.board[nx][ny] == ' ':
                queue.append((nx, ny, 0, (dx, dy)))
                visited.add((nx, ny, 0, (dx, dy)))
    if abs(start_x - end_x) + abs(start_y - end_y) == 1:
        return True
    while queue:
        x, y, turns, direction = queue.popleft()
        if (x, y) == (end_x, end_y):
            return True
        nx, ny = (x + direction[0], y + direction[1])
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if self.board[nx][ny] == ' ' or (nx, ny) == (end_x, end_y):
                if (nx, ny, turns, direction) not in visited:
                    queue.append((nx, ny, turns, direction))
                    visited.add((nx, ny, turns, direction))
        if turns < 2:
            for dx, dy in directions:
                if (dx, dy) != direction and (dx, dy) != (-direction[0], -direction[1]):
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                        if self.board[nx][ny] == ' ' or (nx, ny) == (end_x, end_y):
                            if (nx, ny, turns + 1, (dx, dy)) not in visited:
                                queue.append((nx, ny, turns + 1, (dx, dy)))
                                visited.add((nx, ny, turns + 1, (dx, dy)))
    return False