def remove_icons(self, pos1, pos2):
    """
    rimuove le icone collegate sulla tavola da gioco
    :param pos1: tupla di posizione (x, y) della prima icona da rimuovere
    :param pos2: tupla di posizione (x, y) della seconda icona da rimuovere
    :return: None
    """
    x1, y1 = pos1
    x2, y2 = pos2
    self.board[y1][x1] = ' '
    self.board[y2][x2] = ' '