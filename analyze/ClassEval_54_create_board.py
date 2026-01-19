def create_board(self):
    """
    crea el tablero de juego con el tamaño de tablero y los íconos dados
    :return: lista bidimensional, el tablero de juego
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.create_board()
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    import random
    
    rows, cols = self.board_size[0], self.board_size[1]
    total_cells = rows * cols
    
    # Necesitamos un número par de cada ícono para poder emparejarlos
    tiles = []
    icons_count = len(self.icons)
    
    # Calcular cuántas veces necesitamos cada ícono (siempre en pares)
    tiles_per_icon = total_cells // icons_count
    
    # Crear la lista de fichas asegurando que haya pares
    for icon in self.icons:
        tiles.extend([icon] * tiles_per_icon)
    
    # Si hay celdas restantes, agregar más íconos en pares
    remaining = total_cells - len(tiles)
    if remaining > 0:
        for i in range(remaining):
            tiles.append(self.icons[i % icons_count])
    
    # Mezclar las fichas
    random.shuffle(tiles)
    
    # Crear el tablero bidimensional
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[index])
            index += 1
        board.append(row)
    
    self.board = board
    return board