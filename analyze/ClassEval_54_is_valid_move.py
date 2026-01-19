def is_valid_move(self, pos1, pos2):
    """
    检查两个图标的移动是否有效（即位置在游戏棋盘范围内，两个位置不相同，两个位置有相同的图标，并且两个位置之间有有效路径）
    :param pos1: 第一个图标的位置元组(x, y)
    :param pos2: 第二个图标的位置元组(x, y)
    :return: True 或 False，表示两个图标的移动是否有效
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    >>> mc.is_valid_move((0, 0), (1, 0))
    True
    """
    # Check if positions are the same
    if pos1 == pos2:
        return False
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # Check if positions are within board bounds
    if not (0 <= y1 < len(self.board) and 0 <= x1 < len(self.board[0])):
        return False
    if not (0 <= y2 < len(self.board) and 0 <= x2 < len(self.board[0])):
        return False
    
    # Check if both positions have the same icon (and not empty)
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Check if positions are not empty (assuming None or empty string means empty)
    if self.board[y1][x1] is None or self.board[y1][x1] == '':
        return False
    
    # Check if there's a valid path between the two positions
    return self.has_valid_path(pos1, pos2)


def has_valid_path(self, pos1, pos2):
    """
    Helper method to check if there's a valid path between two positions.
    A valid path in Mahjong Connect can have at most 2 turns (3 line segments).
    """
    from collections import deque
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # BFS to find path with at most 2 turns
    # State: (x, y, direction, turns)
    # direction: 0=right, 1=down, 2=left, 3=up, -1=start
    queue = deque([(x1, y1, -1, 0)])
    visited = set()
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, up
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        if (x, y) == (x2, y2):
            return True
        
        state = (x, y, prev_dir, turns)
        if state in visited:
            continue
        visited.add(state)
        
        # Try all 4 directions
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Check bounds (allow one step outside the board)
            if -1 <= ny <= len(self.board) and -1 <= nx <= len(self.board[0]):
                # Calculate new turn count
                new_turns = turns
                if prev_dir != -1 and prev_dir != dir_idx:
                    new_turns += 1
                
                # Can't have more than 2 turns
                if new_turns > 2:
                    continue
                
                # Check if position is valid (empty or target)
                if (nx, ny) == (x2, y2):
                    queue.append((nx, ny, dir_idx, new_turns))
                elif 0 <= ny < len(self.board) and 0 <= nx < len(self.board[0]):
                    if self.board[ny][nx] is None or self.board[ny][nx] == '':
                        queue.append((nx, ny, dir_idx, new_turns))
                else:
                    # Outside board, can move through
                    queue.append((nx, ny, dir_idx, new_turns))
    
    return False