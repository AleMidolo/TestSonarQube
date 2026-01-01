def check_win(self):
    """
        Verifica si el juego ha sido ganado. El juego se gana cuando todas las cajas están colocadas en las posiciones objetivo.
        Y actualiza el valor de self.is_game_over.
        :return self.is_game_over: True si todas las cajas están colocadas en las posiciones objetivo, o False en caso contrario.
        >>> juego = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> juego.check_win()
        """
    for box in self.boxes:
        if box not in self.targets:
            self.is_game_over = False
            return self.is_game_over
    self.is_game_over = True
    return self.is_game_over