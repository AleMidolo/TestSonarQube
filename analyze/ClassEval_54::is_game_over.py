def is_game_over(self):
    """
        Controlla se il gioco è finito (cioè, se non ci sono più icone sulla tavola di gioco)
        :return: True o False, che rappresenta se il gioco è finito
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
    for row in self.board:
        for cell in row:
            if cell != ' ':
                return False
    return True