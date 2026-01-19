def check_win(self):
    """
    Verifica si el juego ha sido ganado. El juego se gana cuando todas las cajas están colocadas en las posiciones objetivo.
    Y actualiza el valor de self.is_game_over.
    :return self.is_game_over: True si todas las cajas están colocadas en las posiciones objetivo, o False en caso contrario.
    >>> juego = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
    >>> juego.check_win()
    """
    # Verificar si todas las posiciones objetivo tienen una caja
    for goal_pos in self.goals:
        if goal_pos not in self.boxes:
            self.is_game_over = False
            return self.is_game_over
    
    # Si todas las cajas están en posiciones objetivo
    self.is_game_over = True
    return self.is_game_over