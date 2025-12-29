def check_win(self):
    """
        Controlla se il gioco è vinto. Il gioco è vinto quando tutte le scatole sono posizionate nelle posizioni target.
        E aggiorna il valore di self.is_game_over.
        :return self.is_game_over: True se tutte le scatole sono posizionate nelle posizioni target, altrimenti False.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
    all_boxes_on_target = all((box in self.targets for box in self.boxes))
    self.is_game_over = all_boxes_on_target
    return self.is_game_over