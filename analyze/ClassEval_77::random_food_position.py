def random_food_position(self):
    """
        यादृच्छिक रूप से एक नया खाद्य स्थान उत्पन्न करें, लेकिन इसे सांप पर न रखें।
        :return: कुछ नहीं, खाद्य स्थान बदलें
        """
    while True:
        new_food_position = (random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE, random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE)
        if new_food_position not in self.positions:
            self.food_position = new_food_position
            break