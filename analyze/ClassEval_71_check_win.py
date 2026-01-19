def check_win(self):
    """
    खेल जीतने की जांच करें। खेल तब जीता जाता है जब सभी बॉक्स लक्षित स्थानों पर रखे जाते हैं।
    और self.is_game_over का मान अपडेट करें।
    :return self.is_game_over: यदि सभी बॉक्स लक्षित स्थानों पर रखे गए हैं, तो True, अन्यथा False।
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> game.check_win()
    """
    # सभी बॉक्स के स्थानों को खोजें
    boxes = set()
    targets = set()
    
    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            if self.grid[i][j] == 'X':  # बॉक्स
                boxes.add((i, j))
            if self.grid[i][j] == 'G':  # लक्षित स्थान
                targets.add((i, j))
    
    # जांचें कि सभी लक्षित स्थानों पर बॉक्स हैं या नहीं
    # खेल जीता जाता है जब सभी बॉक्स लक्षित स्थानों पर हों
    self.is_game_over = boxes == targets and len(targets) > 0
    
    return self.is_game_over