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
        nx, ny = (start_x + dx, start_y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ':
                queue.append((nx, ny, 0, i))
                visited.add((nx, ny, 0, i))
    if abs(start_x - end_x) + abs(start_y - end_y) == 1:
        return True
    while queue:
        x, y, turns, direction = queue.popleft()
        dx, dy = directions[direction]
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ' and (nx, ny, turns, direction) not in visited:
                queue.append((nx, ny, turns, direction))
                visited.add((nx, ny, turns, direction))
        if turns < 2:
            for new_dir in range(4):
                if new_dir == direction:
                    continue
                dx, dy = directions[new_dir]
                nx, ny = (x + dx, y + dy)
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                    if (nx, ny) == (end_x, end_y):
                        return True
                    if self.board[nx][ny] == ' ' and (nx, ny, turns + 1, new_dir) not in visited:
                        queue.append((nx, ny, turns + 1, new_dir))
                        visited.add((nx, ny, turns + 1, new_dir))
    return False