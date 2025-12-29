def has_path(self, pos1, pos2):
    """
        检查两个图标之间是否存在路径
        :param pos1: 第一个图标的位置元组(x, y)
        :param pos2: 第二个图标的位置元组(x, y)
        :return: True 或 False，表示两个图标之间是否存在路径
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
        nx, ny = (x + direction[0], y + direction[1])
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if self.board[nx][ny] == ' ' or (nx, ny) == (end_x, end_y):
                if (nx, ny, turns, direction) not in visited:
                    queue.append((nx, ny, turns, direction))
                    visited.add((nx, ny, turns, direction))
        if turns < 2:
            for dx, dy in directions:
                if (dx, dy) == direction or (dx, dy) == (-direction[0], -direction[1]):
                    continue
                nx, ny = (x + dx, y + dy)
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                    if self.board[nx][ny] == ' ' or (nx, ny) == (end_x, end_y):
                        if (nx, ny, turns + 1, (dx, dy)) not in visited:
                            queue.append((nx, ny, turns + 1, (dx, dy)))
                            visited.add((nx, ny, turns + 1, (dx, dy)))
    return False