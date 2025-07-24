import random

class MinesweeperGame:
    def __init__(self, n, k) -> None:
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_player_map()
        self.score = 0

    def generate_mine_sweeper_map(self):
        arr = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for _ in range(self.k):
            x, y = self.place_mine(arr)
            self.update_adjacent_cells(arr, x, y)
        return arr

    def place_mine(self, arr):
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        arr[y][x] = 'X'
        return x, y

    def update_adjacent_cells(self, arr, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n and arr[ny][nx] != 'X':
                    arr[ny][nx] += 1

    def generate_player_map(self):
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        if self.minesweeper_map[x][y] == 'X':
            return False
        self.player_map[x][y] = self.minesweeper_map[x][y]
        self.score += 1
        return self.check_won()  # Return the result of check_won directly