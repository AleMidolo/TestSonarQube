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
    queue.append((x1, y1, 0, None))
    visited.add((x1, y1))
    while queue:
        x, y, turns, prev_dir = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                if self.board[nx][ny] == ' ' or (nx, ny) == (x2, y2):
                    if prev_dir is None:
                        new_turns = 0
                    elif (dx, dy) != prev_dir:
                        new_turns = turns + 1
                    else:
                        new_turns = turns
                    if new_turns <= 2 and (nx, ny) not in visited:
                        queue.append((nx, ny, new_turns, (dx, dy)))
                        visited.add((nx, ny))
    return False