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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    start_x, start_y = pos1
    end_x, end_y = pos2
    for dx, dy in directions:
        nx, ny = (start_x + dx, start_y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ':
                queue.append((nx, ny, 0, (dx, dy)))
                visited.add((nx, ny, 0, (dx, dy)))
    while queue:
        x, y, turns, direction = queue.popleft()
        if turns > 2:
            continue
        nx, ny = (x + direction[0], y + direction[1])
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ' and (nx, ny, turns, direction) not in visited:
                queue.append((nx, ny, turns, direction))
                visited.add((nx, ny, turns, direction))
        for dx, dy in directions:
            if (dx, dy) == direction or (dx, dy) == (-direction[0], -direction[1]):
                continue
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                if (nx, ny) == (end_x, end_y):
                    return True
                if self.board[nx][ny] == ' ' and (nx, ny, turns + 1, (dx, dy)) not in visited:
                    queue.append((nx, ny, turns + 1, (dx, dy)))
                    visited.add((nx, ny, turns + 1, (dx, dy)))
    return False