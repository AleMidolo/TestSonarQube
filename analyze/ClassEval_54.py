import random


class MahjongConnect:
    EMPTY_ICON = ' '

    def __init__(self, board_size, icons):
        self.board_size = board_size
        self.icons = icons
        self.board = self.create_board()

    def create_board(self):
        return [[random.choice(self.icons) for _ in range(self.board_size[1])] for _ in range(self.board_size[0])]

    def is_valid_move(self, pos1, pos2):
        if not self.are_positions_valid(pos1, pos2):
            return False
        if pos1 == pos2:
            return False
        if not self.icons_match(pos1, pos2):
            return False
        if not self.has_path(pos1, pos2):
            return False
        return True

    def are_positions_valid(self, pos1, pos2):
        return (self.is_within_bounds(pos1) and self.is_within_bounds(pos2))

    def is_within_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.board_size[0] and 0 <= y < self.board_size[1]

    def icons_match(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return self.board[x1][y1] == self.board[x2][y2]

    def has_path(self, pos1, pos2):
        visited = set()
        stack = [pos1]

        while stack:
            current_pos = stack.pop()
            if current_pos == pos2:
                return True
            if current_pos in visited:
                continue
            visited.add(current_pos)
            self.add_adjacent_positions_to_stack(current_pos, stack, visited)

        return False

    def add_adjacent_positions_to_stack(self, current_pos, stack, visited):
        x, y = current_pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if self.is_within_bounds((new_x, new_y)) and (new_x, new_y) not in visited and self.board[new_x][new_y] == self.board[x][y]:
                stack.append((new_x, new_y))

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = self.EMPTY_ICON
        self.board[pos2[0]][pos2[1]] = self.EMPTY_ICON

    def is_game_over(self):
        return all(icon == self.EMPTY_ICON for row in self.board for icon in row)