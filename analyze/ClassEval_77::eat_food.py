def eat_food(self):
    """
        साँप की लंबाई को 1 से बढ़ाएं और स्कोर को 100 से बढ़ाएं। एक नई खाद्य स्थिति को यादृच्छिक रूप से उत्पन्न करें, लेकिन
        इसे साँप पर न रखें।
        :return: कुछ नहीं
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.move((1,1))
        >>> snake.eat_food()
        self.length = 2
        self.score = 10
        """
    self.length += 1
    self.score += 100
    self.random_food_position()