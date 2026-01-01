def has_path(self, pos1, pos2):
    """
        controlla se c'è un percorso tra due icone
        :param pos1: tupla di posizione(x, y) della prima icona
        :param pos2: tupla di posizione(x, y) della seconda icona
        :return: True o False, che rappresenta se c'è un percorso tra due icone
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
        dx, dy = direction
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ' and (nx, ny, turns, direction) not in visited:
                queue.append((nx, ny, turns, direction))
                visited.add((nx, ny, turns, direction))
        for new_dx, new_dy in directions:
            if (new_dx, new_dy) == direction or (new_dx, new_dy) == (-dx, -dy):
                continue
            nx, ny = (x + new_dx, y + new_dy)
            if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                if (nx, ny) == (end_x, end_y):
                    return True
                if self.board[nx][ny] == ' ' and (nx, ny, turns + 1, (new_dx, new_dy)) not in visited:
                    queue.append((nx, ny, turns + 1, (new_dx, new_dy)))
                    visited.add((nx, ny, turns + 1, (new_dx, new_dy)))
    return False