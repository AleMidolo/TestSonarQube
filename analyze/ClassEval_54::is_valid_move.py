def is_valid_move(self, pos1, pos2):
        """
        verifica se il movimento di due icone è valido (cioè le posizioni sono all'interno dell'intervallo della tavola da gioco, le due posizioni non sono le stesse, le due posizioni hanno la stessa icona e c'è un percorso valido tra le due posizioni)
        :param pos1: tupla di posizione (x, y) della prima icona
        :param pos2: tupla di posizione (x, y) della seconda icona
        :return: True o False, che rappresenta se il movimento di due icone è valido
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        if pos1 == pos2:
            return False
        
        x1, y1 = pos1
        x2, y2 = pos2
        
        if not (0 <= x1 < self.BOARD_SIZE[0] and 0 <= y1 < self.BOARD_SIZE[1]):
            return False
        if not (0 <= x2 < self.BOARD_SIZE[0] and 0 <= y2 < self.BOARD_SIZE[1]):
            return False
        
        if self.board[x1][y1] != self.board[x2][y2]:
            return False
        
        return self.has_path(pos1, pos2)