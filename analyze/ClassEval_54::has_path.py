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
    visited = set()
    queue = deque()
    queue.append((x1, y1, None, 0))
    visited.add((x1, y1, None, 0))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        if (x, y) == (x2, y2):
            return True
        for dx, dy in directions:
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if (new_x, new_y) != (x2, y2) and self.board[new_x][new_y] != ' ':
                continue
            new_dir = (dx, dy)
            new_turns = turns
            if prev_dir is not None and new_dir != prev_dir:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_dir, new_turns)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False