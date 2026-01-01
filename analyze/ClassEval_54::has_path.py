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
    from collections import deque

    def is_valid(x, y):
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1] and (self.board[x][y] == self.board[pos1[0]][pos1[1]])
    queue = deque([pos1])
    visited = set()
    visited.add(pos1)
    while queue:
        current = queue.popleft()
        if current == pos2:
            return True
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = (x + dx, y + dy)
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False