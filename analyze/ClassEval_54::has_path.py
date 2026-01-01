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
    if abs(x1 - x2) + abs(y1 - y2) == 1:
        return True
    rows, cols = (self.BOARD_SIZE[0], self.BOARD_SIZE[1])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited[x1][y1] = True
    for dx, dy in directions:
        nx, ny = (x1 + dx, y1 + dy)
        if 0 <= nx < rows and 0 <= ny < cols and (self.board[nx][ny] == ' ' or (nx == x2 and ny == y2)):
            queue.append((nx, ny, 0, (dx, dy)))
            visited[nx][ny] = True
    while queue:
        x, y, turns, dir = queue.popleft()
        if x == x2 and y == y2:
            return True
        if turns >= 2:
            continue
        nx, ny = (x + dir[0], y + dir[1])
        if 0 <= nx < rows and 0 <= ny < cols and (not visited[nx][ny]) and (self.board[nx][ny] == ' ' or (nx == x2 and ny == y2)):
            queue.append((nx, ny, turns, dir))
            visited[nx][ny] = True
        for dx, dy in directions:
            if (dx, dy) == dir or (dx, dy) == (-dir[0], -dir[1]):
                continue
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < rows and 0 <= ny < cols and (not visited[nx][ny]) and (self.board[nx][ny] == ' ' or (nx == x2 and ny == y2)):
                queue.append((nx, ny, turns + 1, (dx, dy)))
                visited[nx][ny] = True
    return False