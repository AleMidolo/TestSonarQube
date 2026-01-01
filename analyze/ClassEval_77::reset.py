def reset(self):
    """
        सांप को इसके प्रारंभिक स्थिति में रीसेट करें। लंबाई को 1 पर सेट करें, सांप के सिर की स्थिति को ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)) पर सेट करें, स्कोर को 0 पर सेट करें, और नए खाद्य स्थिति को यादृच्छिक रूप से उत्पन्न करें।
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.reset()
        self.length = 1
        self.positions = [(50, 50)]
        self.score = 0
        self.random_food_position()
        """
    self.length = 1
    self.positions = [(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)]
    self.score = 0
    self.random_food_position()