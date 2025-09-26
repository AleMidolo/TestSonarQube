import random


class MahjongConnect:
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
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def are_positions_valid(self, pos1, pos2):
        return (0 <= pos1[0] < self.board_size[0] and 0 <= pos1[1] < self.board_size[1] and
                0 <= pos2[0] < self.board_size[0] and 0 <= pos2[1] < self.board_size[1])

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
            self.add_adjacent_positions_to_stack(current_pos, visited, stack)

        return False

    def add_adjacent_positions_to_stack(self, current_pos, visited, stack):
        x, y = current_pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.board_size[0] and 0 <= new_y < self.board_size[1] and
                    (new_x, new_y) not in visited and self.board[new_x][new_y] == self.board[x][y]):
                stack.append((new_x, new_y))

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        return all(icon == ' ' for row in self.board for icon in row)