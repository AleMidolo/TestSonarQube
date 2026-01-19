def check_win(self):
    """
    खेल जीतने की जांच करें। खेल तब जीता जाता है जब सभी बॉक्स लक्षित स्थानों पर रखे जाते हैं।
    और self.is_game_over का मान अपडेट करें।
    :return self.is_game_over: यदि सभी बॉक्स लक्षित स्थानों पर रखे गए हैं, तो True, अन्यथा False।
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> game.check_win()
    """
    # सभी बॉक्स (X) के स्थानों को खोजें
    boxes = set()
    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            if self.grid[i][j] == 'X':
                boxes.add((i, j))
    
    # सभी लक्षित स्थानों (G) को खोजें
    goals = set()
    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            if self.grid[i][j] == 'G':
                goals.add((i, j))
    
    # जांचें कि सभी बॉक्स लक्षित स्थानों पर हैं या नहीं
    # खेल जीता जाता है जब सभी लक्षित स्थानों पर बॉक्स हों
    self.is_game_over = len(goals) > 0 and boxes == goals
    
    return self.is_game_over