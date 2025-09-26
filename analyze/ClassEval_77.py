import random


class Snake:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [self.initial_position()]
        self.score = 0
        self.food_position = food_position

    def initial_position(self):
        return (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)

    def move(self, direction):
        cur = self.positions[0]
        new = self.calculate_new_position(cur, direction)

        if new == self.food_position:
            self.eat_food()

        if self.is_collision(new):
            self.reset()
        else:
            self.update_position(new)

    def calculate_new_position(self, cur, direction):
        x, y = direction
        return (
            (cur[0] + (x * self.BLOCK_SIZE)) % self.SCREEN_WIDTH,
            (cur[1] + (y * self.BLOCK_SIZE)) % self.SCREEN_HEIGHT,
        )

    def is_collision(self, new):
        return len(self.positions) > 2 and new in self.positions[2:]

    def update_position(self, new):
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def random_food_position(self):
        while self.food_position in self.positions:
            self.food_position = self.generate_random_food_position()

    def generate_random_food_position(self):
        return (
            random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE,
            random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE
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