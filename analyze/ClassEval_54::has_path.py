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

    def is_within_bounds(x, y):
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

    def bfs(start, end):
        queue = deque([start])
        visited = set()
        visited.add(start)
        while queue:
            current = queue.popleft()
            if current == end:
                return True
            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (x + dx, y + dy)
                if is_within_bounds(neighbor[0], neighbor[1]) and neighbor not in visited and (self.board[neighbor[0]][neighbor[1]] == self.board[x][y]):
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
    return bfs(pos1, pos2)