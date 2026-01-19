def create_board(self):
    """
    crea la tavola di gioco con la dimensione della tavola e le icone date
    :return: lista bidimensionale, la tavola di gioco
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.create_board()
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    rows, cols = self.size[0], self.size[1]
    total_cells = rows * cols
    
    # Calculate how many pairs of each icon we need
    pairs_needed = total_cells // 2
    
    # Create a flat list with pairs of icons
    tiles = []
    icon_index = 0
    for _ in range(pairs_needed):
        icon = self.icons[icon_index % len(self.icons)]
        tiles.extend([icon, icon])
        icon_index += 1
    
    # Create the board by distributing tiles row by row
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