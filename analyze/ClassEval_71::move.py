def move(self, direction):
    """
        Mueve al jugador según la dirección especificada y verifica si el juego ha sido ganado.
        :param direction: str, la dirección del movimiento del jugador. 
            Puede ser 'w', 's', 'a' o 'd' que representan arriba, abajo, izquierda o derecha respectivamente.

        :return: True si el juego ha sido ganado, False en caso contrario.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
    dir_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in dir_map:
        return self.is_game_over
    dr, dc = dir_map[direction]
    new_row = self.player_row + dr
    new_col = self.player_col + dc
    if new_row < 0 or new_row >= len(self.map) or new_col < 0 or (new_col >= len(self.map[0])) or (self.map[new_row][new_col] == '#'):
        return self.is_game_over
    box_index = -1
    for i, box in enumerate(self.boxes):
        if box == (new_row, new_col):
            box_index = i
            break
    if box_index != -1:
        box_new_row = new_row + dr
        box_new_col = new_col + dc
        if box_new_row < 0 or box_new_row >= len(self.map) or box_new_col < 0 or (box_new_col >= len(self.map[0])) or (self.map[box_new_row][box_new_col] == '#') or ((box_new_row, box_new_col) in self.boxes):
            return self.is_game_over
        self.boxes[box_index] = (box_new_row, box_new_col)
    self.player_row = new_row
    self.player_col = new_col
    self.check_win()
    return self.is_game_over