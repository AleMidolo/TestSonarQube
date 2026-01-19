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
    tiles_per_icon = total_cells // len(self.icons)
    
    # Create a flat list of tiles
    tiles = []
    for icon in self.icons:
        tiles.extend([icon] * tiles_per_icon)
    
    # Fill remaining cells if total_cells is not evenly divisible
    remaining = total_cells - len(tiles)
    for i in range(remaining):
        tiles.append(self.icons[i % len(self.icons)])
    
    # Create the board by reshaping the flat list
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[i * cols + j])
        board.append(row)
    
    self.board = board
    return board