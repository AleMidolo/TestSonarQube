def remove_icons(self, pos1, pos2):
    """
    elimina los íconos conectados en el tablero de juego
    :param pos1: tupla de posición (x, y) del primer ícono a eliminar
    :param pos2: tupla de posición (x, y) del segundo ícono a eliminar
    :return: None
    """
    x1, y1 = pos1
    x2, y2 = pos2
    self.board[y1][x1] = ' '
    self.board[y2][x2] = ' '