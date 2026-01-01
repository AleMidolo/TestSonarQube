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
    if pos1 == pos2:
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    start_x, start_y = pos1
    queue.append((start_x, start_y, 0, -1))
    visited.add((start_x, start_y, 0, -1))
    target_x, target_y = pos2
    while queue:
        x, y, turns, dir_idx = queue.popleft()
        if (x, y) == (target_x, target_y):
            return True
        for new_dir_idx, (dx, dy) in enumerate(directions):
            new_x, new_y = (x + dx, y + dy)
            if not (0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]):
                continue
            if self.board[new_x][new_y] != ' ' and (new_x, new_y) != (target_x, target_y) and ((new_x, new_y) != (start_x, start_y)):
                continue
            new_turns = turns
            if dir_idx != -1 and new_dir_idx != dir_idx:
                new_turns += 1
            if new_turns > 2:
                continue
            state = (new_x, new_y, new_turns, new_dir_idx)
            if state in visited:
                continue
            visited.add(state)
            queue.append(state)
    return False