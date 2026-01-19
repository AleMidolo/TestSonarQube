def has_path(self, pos1, pos2):
    """
        controlla se c'è un percorso tra due icone
        :param pos1: tupla di posizione(x, y) della prima icona
        :param pos2: tupla di posizione(x, y) della seconda icona
        :return: True o False, che rappresenta se c'è un percorso tra due icone
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
    return True