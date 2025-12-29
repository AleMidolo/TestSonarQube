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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    queue.append((x1, y1, 0, -1))
    visited.add((x1, y1, 0, -1))
    while queue:
        x, y, turns, prev_dir = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = (x + dx, y + dy)
            if not (0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]):
                continue
            if (nx, ny) != (x2, y2) and self.board[nx][ny] != ' ':
                continue
            new_turns = turns
            if prev_dir != -1 and dir_idx != prev_dir:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (nx, ny, new_turns, dir_idx)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False