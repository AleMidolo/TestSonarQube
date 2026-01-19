def check_win(self):
    """
    Controlla se il gioco è vinto. Il gioco è vinto quando tutte le scatole sono posizionate nelle posizioni target.
    E aggiorna il valore di self.is_game_over.
    :return self.is_game_over: True se tutte le scatole sono posizionate nelle posizioni target, altrimenti False.
    >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> game.check_win()
    """
    # Verifica se tutte le posizioni delle scatole coincidono con le posizioni target
    if set(self.boxes) == set(self.targets):
        self.is_game_over = True
    else:
        self.is_game_over = False
    
    return self.is_game_over