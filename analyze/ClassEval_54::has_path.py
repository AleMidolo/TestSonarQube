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
            if self.board[nx][ny] == ' ' or (nx == end_x and ny == end_y):
                queue.append((nx, ny, 0, (dx, dy)))
                visited.add((nx, ny, 0, (dx, dy)))
    while queue:
        x, y, turns, direction = queue.popleft()
        if x == end_x and y == end_y:
            return True
        if turns >= 2:
            continue
        dx, dy = direction
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (self.board[nx][ny] == ' ' or (nx == end_x and ny == end_y)) and (nx, ny, turns, direction) not in visited:
                queue.append((nx, ny, turns, direction))
                visited.add((nx, ny, turns, direction))
        for new_dx, new_dy in directions:
            if (new_dx, new_dy) != direction and (new_dx, new_dy) != (-dx, -dy):
                nx, ny = (x + new_dx, y + new_dy)
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                    if (self.board[nx][ny] == ' ' or (nx == end_x and ny == end_y)) and (nx, ny, turns + 1, (new_dx, new_dy)) not in visited:
                        queue.append((nx, ny, turns + 1, (new_dx, new_dy)))
                        visited.add((nx, ny, turns + 1, (new_dx, new_dy)))
    return False