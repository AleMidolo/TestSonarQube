def check_won(self, map):
    """
    Verifica si el jugador ha ganado el juego. Si solo hay minas en el mapa del jugador, devuelve True, de lo contrario devuelve False.
    :return: True si el jugador ha ganado el juego, False en caso contrario.
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> minesweeper_game.check_won(minesweeper_game.player_map)
    False

    """
    for i in range(len(map)):
        for j in range(len(map[i])):
            # Si encontramos una celda no revelada ('-') que no es una mina
            if map[i][j] == '-':
                # Verificamos si en el mapa real hay una mina
                if self.minesweeper_map[i][j] != 'X':
                    # Hay celdas sin revelar que no son minas, no ha ganado
                    return False
    # Todas las celdas no reveladas son minas, el jugador ha ganado
    return True