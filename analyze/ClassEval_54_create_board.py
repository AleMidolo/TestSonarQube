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
    
    # Calcular cuántas parejas de cada ícono necesitamos
    pairs_needed = total_cells // 2
    pairs_per_icon = pairs_needed // icons_count
    remaining_pairs = pairs_needed % icons_count
    
    # Crear las fichas (cada ícono aparece un número par de veces)
    for i, icon in enumerate(self.icons):
        count = pairs_per_icon * 2
        if i < remaining_pairs:
            count += 2
        tiles.extend([icon] * count)
    
    # Mezclar las fichas
    random.shuffle(tiles)
    
    # Crear el tablero bidimensional
    board = []
    tile_index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[tile_index])
            tile_index += 1
        board.append(row)
    
    self.board = board
    return board