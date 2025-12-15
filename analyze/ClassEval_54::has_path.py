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
                    nx, ny = x + dx, y + dy
                    if is_within_bounds(nx, ny) and (nx, ny) not in visited and self.board[nx][ny] != ' ':
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return False

        return bfs(pos1, pos2)