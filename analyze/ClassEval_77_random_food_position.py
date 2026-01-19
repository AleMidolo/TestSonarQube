def random_food_position(self):
    """
    यादृच्छिक रूप से एक नया खाद्य स्थान उत्पन्न करें, लेकिन इसे सांप पर न रखें।
    :return: कुछ नहीं, खाद्य स्थान बदलें
    """
    import random
    
    while True:
        # Generate random x and y coordinates for food
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        
        # Check if this position is not occupied by the snake
        if (x, y) not in self.snake_body:
            self.food_position = (x, y)
            break