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
        queue.append((start_x, start_y, 0, (dx, dy)))
        visited.add((start_x, start_y, 0, (dx, dy)))
    while queue:
        x, y, turns, direction = queue.popleft()
        if (x, y) == (end_x, end_y):
            return True
        for dx, dy in directions:
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (end_x, end_y) and self.board[new_x][new_y] != ' ':
                continue
            new_turns = turns
            if (dx, dy) != direction:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_turns, (dx, dy))
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False