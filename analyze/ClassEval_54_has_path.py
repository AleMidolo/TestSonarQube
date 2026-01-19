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
    visited = set()
    queue = deque()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = (x1 + dx, y1 + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if self.board[nx][ny] == ' ' or (nx == x2 and ny == y2):
                queue.append(((nx, ny), (dx, dy), 0))
                visited.add(((nx, ny), (dx, dy)))
    while queue:
        (x, y), (dx, dy), turns = queue.popleft()
        if x == x2 and y == y2:
            return True
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
            if self.board[nx][ny] == ' ' or (nx == x2 and ny == y2):
                state = ((nx, ny), (dx, dy))
                if state not in visited:
                    visited.add(state)
                    queue.append(((nx, ny), (dx, dy), turns))
        if turns < 2:
            for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (ndx, ndy) == (dx, dy) or (ndx, ndy) == (-dx, -dy):
                    continue
                nx, ny = (x + ndx, y + ndy)
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1]:
                    if self.board[nx][ny] == ' ' or (nx == x2 and ny == y2):
                        state = ((nx, ny), (ndx, ndy))
                        if state not in visited:
                            visited.add(state)
                            queue.append(((nx, ny), (ndx, ndy), turns + 1))
    return False