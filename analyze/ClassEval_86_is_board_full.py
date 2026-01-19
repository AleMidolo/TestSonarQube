def is_board_full(self):
    """
    Controlla se il tabellone di gioco è completamente riempito.
    :return: bool, che indica se il tabellone di gioco è pieno o meno
    >>> ttt.is_board_full()
    False
    """
    for row in self.board:
        for cell in row:
            if cell == ' ' or cell == '':
                return False
    return True