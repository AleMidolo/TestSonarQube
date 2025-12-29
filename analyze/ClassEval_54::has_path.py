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
        x, y, dir_x, dir_y, turns = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        for dx, dy in directions:
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (x2, y2) and self.board[new_x][new_y] != ' ':
                continue
            new_dir_x, new_dir_y = (dx, dy)
            new_turns = turns
            if (dir_x, dir_y) != (0, 0) and (dir_x, dir_y) != (new_dir_x, new_dir_y):
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_dir_x, new_dir_y, new_turns)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False