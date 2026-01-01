def remove_icons(self, pos1, pos2):
    """
        rimuove le icone collegate sulla tavola da gioco
        :param pos1: tupla di posizione (x, y) della prima icona da rimuovere
        :param pos2: tupla di posizione (x, y) della seconda icona da rimuovere
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.remove_icons((0, 0), (1, 0))
        mc.board = [[' ', 'b', 'c', 'a'],
                    [' ', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
    x1, y1 = pos1
    x2, y2 = pos2
    self.board[x1][y1] = ' '
    self.board[x2][y2] = ' '