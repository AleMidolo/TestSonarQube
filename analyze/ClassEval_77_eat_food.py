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
    import random
    
    # साँप की लंबाई को 1 से बढ़ाएं
    self.length += 1
    
    # स्कोर को 100 से बढ़ाएं
    self.score += 100
    
    # एक नई खाद्य स्थिति को यादृच्छिक रूप से उत्पन्न करें
    # जो साँप के शरीर पर न हो
    while True:
        new_food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        # जांचें कि नई खाद्य स्थिति साँप के शरीर पर नहीं है
        if new_food not in self.body:
            self.food = new_food
            break