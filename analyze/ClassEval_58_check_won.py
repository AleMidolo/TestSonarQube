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
            # Si hay una celda sin revelar ('-') en el mapa del jugador
            if map[i][j] == '-':
                # Verificar si esa posición NO es una mina en el mapa real
                if self.minesweeper_map[i][j] != 'X':
                    # Todavía hay celdas seguras sin revelar, no ha ganado
                    return False
    # Todas las celdas no-mina han sido reveladas
    return True