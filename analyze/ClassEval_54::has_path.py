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
        queue.append((start_x, start_y, 0, (dx, dy)))
        visited.add((start_x, start_y, 0, (dx, dy)))
    if abs(start_x - end_x) + abs(start_y - end_y) == 1:
        return True
    while queue:
        x, y, turns, (dx, dy) = queue.popleft()
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if (nx, ny) == (end_x, end_y):
                return True
            if self.board[nx][ny] == ' ':
                if (nx, ny, turns, (dx, dy)) not in visited:
                    queue.append((nx, ny, turns, (dx, dy)))
                    visited.add((nx, ny, turns, (dx, dy)))
            if turns < 2:
                for ndx, ndy in directions:
                    if (ndx, ndy) == (dx, dy) or (ndx, ndy) == (-dx, -dy):
                        continue
                    nnx, nny = (x + ndx, y + ndy)
                    if 0 <= nnx < self.BOARD_SIZE[0] and 0 <= nny < self.BOARD_SIZE[1]:
                        if (nnx, nny) == (end_x, end_y):
                            return True
                        if self.board[nnx][nny] == ' ':
                            if (nnx, nny, turns + 1, (ndx, ndy)) not in visited:
                                queue.append((nnx, nny, turns + 1, (ndx, ndy)))
                                visited.add((nnx, nny, turns + 1, (ndx, ndy)))
    return False