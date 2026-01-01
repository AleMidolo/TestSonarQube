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
    direction_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in direction_map:
        return False
    new_player_row = self.player_row + direction_map[direction][0]
    new_player_col = self.player_col + direction_map[direction][1]
    if self.map[new_player_row][new_player_col] == '#':
        return False
    if (new_player_row, new_player_col) in self.boxes:
        new_box_row = new_player_row + direction_map[direction][0]
        new_box_col = new_player_col + direction_map[direction][1]
        if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
            return False
        self.boxes.remove((new_player_row, new_player_col))
        self.boxes.append((new_box_row, new_box_col))
    self.player_row = new_player_row
    self.player_col = new_player_col
    return self.check_win()