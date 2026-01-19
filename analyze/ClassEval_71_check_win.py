def check_win(self):
    """
        खेल जीतने की जांच करें। खेल तब जीता जाता है जब सभी बॉक्स लक्षित स्थानों पर रखे जाते हैं।
        और self.is_game_over का मान अपडेट करें।
        :return self.is_game_over: यदि सभी बॉक्स लक्षित स्थानों पर रखे गए हैं, तो True, अन्यथा False।
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
    all_boxes_on_targets = all((box in self.targets for box in self.boxes))
    self.is_game_over = all_boxes_on_targets
    return self.is_game_over