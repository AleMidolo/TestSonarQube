def check_win(self):
    """
        Verifica si el juego ha sido ganado. El juego se gana cuando todas las cajas están colocadas en las posiciones objetivo.
        Y actualiza el valor de self.is_game_over.
        :return self.is_game_over: True si todas las cajas están colocadas en las posiciones objetivo, o False en caso contrario.
        >>> juego = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> juego.check_win()
        """
    self.is_game_over = all((box in self.targets for box in self.boxes))
    return self.is_game_over