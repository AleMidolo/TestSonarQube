class PushBoxGame:
    def __init__(self, map):
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False

        self.init_game()

    def init_game(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                self._initialize_player_and_targets(row, col)

    def _initialize_player_and_targets(self, row, col):
        if self.map[row][col] == "O":
            self.player_row = row
            self.player_col = col
        elif self.map[row][col] == "G":
            self.targets.append((row, col))
            self.target_count += 1
        elif self.map[row][col] == "X":
            self.boxes.append((row, col))

    def check_win(self):
        box_on_target_count = self._count_boxes_on_targets()
        if box_on_target_count == self.target_count:
            self.is_game_over = True
        return self.is_game_over

    def _count_boxes_on_targets(self):
        return sum(1 for box in self.boxes if box in self.targets)

    def move(self, direction):
        new_player_row, new_player_col = self._calculate_new_player_position(direction)

        if self._is_valid_move(new_player_row, new_player_col):
            if (new_player_row, new_player_col) in self.boxes:
                self._move_box(new_player_row, new_player_col)
            else:
                self.player_row = new_player_row
                self.player_col = new_player_col

        return self.check_win()

    def _calculate_new_player_position(self, direction):
        new_player_row = self.player_row
        new_player_col = self.player_col

        if direction == "w":
            new_player_row -= 1
        elif direction == "s":
            new_player_row += 1
        elif direction == "a":
            new_player_col -= 1
        elif direction == "d":
            new_player_col += 1

        return new_player_row, new_player_col

    def _is_valid_move(self, new_player_row, new_player_col):
        return self.map[new_player_row][new_player_col] != "#"

    def _move_box(self, new_player_row, new_player_col):
        new_box_row = new_player_row + (new_player_row - self.player_row)
        new_box_col = new_player_col + (new_player_col - self.player_col)

        if self.map[new_box_row][new_box_col] != "#":
            self.boxes.remove((new_player_row, new_player_col))
            self.boxes.append((new_box_row, new_box_col))
            self.player_row = new_player_row
            self.player_col = new_player_col