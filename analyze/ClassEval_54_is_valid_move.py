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
    rows = len(self.board)
    cols = len(self.board[0]) if rows > 0 else 0
    
    if not (0 <= x1 < cols and 0 <= y1 < rows):
        return False
    if not (0 <= x2 < cols and 0 <= y2 < rows):
        return False
    
    # Check if both positions have the same icon (and not empty)
    if self.board[y1][x1] != self.board[y2][x2]:
        return False
    
    # Check if positions are not empty (assuming None or empty string means empty)
    if self.board[y1][x1] is None or self.board[y1][x1] == '':
        return False
    
    # Check if there's a valid path between the two positions
    return self._has_valid_path(pos1, pos2)

def _has_valid_path(self, pos1, pos2):
    """
    Helper method to check if there's a valid path between two positions.
    A valid path in Mahjong Connect can have at most 2 turns (3 line segments).
    """
    from collections import deque
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # BFS with direction and turn count tracking
    queue = deque([(x1, y1, -1, 0)])  # (x, y, direction, turns)
    visited = {}  # (x, y, direction): turns
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # down, up, right, left
    
    while queue:
        x, y, prev_dir, turns = queue.popleft()
        
        # If we reached the target
        if (x, y) == pos2:
            return True
        
        # Try all four directions
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            # Calculate new turn count
            new_turns = turns
            if prev_dir != -1 and prev_dir != dir_idx:
                new_turns += 1
            
            # Maximum 2 turns allowed
            if new_turns > 2:
                continue
            
            # Check bounds (allow one step outside for edge connections)
            if not (-1 <= nx <= len(self.board[0]) and -1 <= ny <= len(self.board)):
                continue
            
            # Check if position is empty or is the target
            if (nx, ny) != pos2:
                if nx < 0 or ny < 0 or nx >= len(self.board[0]) or ny >= len(self.board):
                    # Outside board - can traverse
                    pass
                elif self.board[ny][nx] is not None and self.board[ny][nx] != '':
                    # Position is occupied
                    continue
            
            # Check if we've visited this state with fewer or equal turns
            state = (nx, ny, dir_idx)
            if state in visited and visited[state] <= new_turns:
                continue
            
            visited[state] = new_turns
            queue.append((nx, ny, dir_idx, new_turns))
    
    return False