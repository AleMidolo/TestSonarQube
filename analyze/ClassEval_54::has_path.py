def has_path(self, pos1, pos2):
    """
        दो आइकनों के बीच एक पथ है या नहीं, यह जांचें
        :param pos1: पहले आइकन की स्थिति ट्यूपल(x, y)
        :param pos2: दूसरे आइकन की स्थिति ट्यूपल(x, y)
        :return: True या False, जो दर्शाता है कि दो आइकनों के बीच एक पथ है या नहीं
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
    if pos1 == pos2 or self.board[x1][y1] != self.board[x2][y2]:
        return False
    rows, cols = self.BOARD_SIZE
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited[x1][y1] = True
    for dx, dy in directions:
        nx, ny = (x1 + dx, y1 + dy)
        if 0 <= nx < rows and 0 <= ny < cols and (self.board[nx][ny] == ' ' or (nx == x2 and ny == y2)):
            queue.append((nx, ny, 0, (dx, dy)))
    while queue:
        x, y, turns, dir = queue.popleft()
        if x == x2 and y == y2:
            return True
        if turns >= 2:
            continue
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols:
                if self.board[nx][ny] == ' ' or (nx == x2 and ny == y2):
                    new_turns = turns
                    if (dx, dy) != dir:
                        new_turns = turns + 1
                    if not visited[nx][ny] or new_turns < 2:
                        visited[nx][ny] = True
                        queue.append((nx, ny, new_turns, (dx, dy)))
    return False