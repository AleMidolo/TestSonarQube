def create_board(self):
    """
    create the game board with the given board size and icons
    :return: 2-dimensional list, the game board
    >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    >>> mc.create_board()
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    """
    import random
    
    rows, cols = self.board_size
    total_cells = rows * cols
    
    # Calculate how many of each icon we need (must be even for pairing)
    # We need total_cells tiles, distributed among icons
    tiles_per_icon = total_cells // len(self.icons)
    
    # Create a flat list of all tiles
    tiles = []
    for icon in self.icons:
        tiles.extend([icon] * tiles_per_icon)
    
    # If there are remaining cells due to division, fill with icons cyclically
    remaining = total_cells - len(tiles)
    for i in range(remaining):
        tiles.append(self.icons[i % len(self.icons)])
    
    # Shuffle the tiles
    random.shuffle(tiles)
    
    # Convert flat list to 2D board
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[i * cols + j])
        board.append(row)
    
    self.board = board
    return board