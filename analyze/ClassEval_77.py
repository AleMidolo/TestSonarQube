import random


class Snake:
    def __init__(self, screen_width, screen_height, block_size, food_position):
        self.length = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.positions = [self.initial_position()]
        self.score = 0
        self.food_position = food_position

    def initial_position(self):
        return (self.screen_width / 2, self.screen_height / 2)

    def move(self, direction):
        new_position = self.calculate_new_position(direction)

        if new_position == self.food_position:
            self.eat_food()

        if self.is_collision(new_position):
            self.reset()
        else:
            self.update_positions(new_position)

    def calculate_new_position(self, direction):
        cur = self.positions[0]
        x, y = direction
        return (
            (cur[0] + (x * self.block_size)) % self.screen_width,
            (cur[1] + (y * self.block_size)) % self.screen_height,
        )

    def is_collision(self, new_position):
        return len(self.positions) > 2 and new_position in self.positions[2:]

    def update_positions(self, new_position):
        self.positions.insert(0, new_position)
        if len(self.positions) > self.length:
            self.positions.pop()

    def random_food_position(self):
        while self.food_position in self.positions:
            self.food_position = self.generate_random_food_position()

    def generate_random_food_position(self):
        return (
            random.randint(0, self.screen_width // self.block_size - 1) * self.block_size,
            random.randint(0, self.screen_height // self.block_size - 1) * self.block_size
        )

    def reset(self):
        self.length = 1
        self.positions = [self.initial_position()]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        self.length += 1
        self.score += 100
        self.random_food_position()