def check_win(self):
    """
        Controlla se il gioco è vinto. Il gioco è vinto quando tutte le scatole sono posizionate nelle posizioni target.
        E aggiorna il valore di self.is_game_over.
        :return self.is_game_over: True se tutte le scatole sono posizionate nelle posizioni target, altrimenti False.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
    for box in self.boxes:
        if box not in self.targets:
            self.is_game_over = False
            return self.is_game_over
    self.is_game_over = True
    return self.is_game_over