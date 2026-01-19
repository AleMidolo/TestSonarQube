def check_win(self):
    """
        खेल जीतने की जांच करें। खेल तब जीता जाता है जब सभी बॉक्स लक्षित स्थानों पर रखे जाते हैं।
        और self.is_game_over का मान अपडेट करें।
        :return self.is_game_over: यदि सभी बॉक्स लक्षित स्थानों पर रखे गए हैं, तो True, अन्यथा False।
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
    boxes_on_targets = 0
    for box in self.boxes:
        if box in self.targets:
            boxes_on_targets += 1
    if boxes_on_targets == self.target_count:
        self.is_game_over = True
    else:
        self.is_game_over = False
    return self.is_game_over