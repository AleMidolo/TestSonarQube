def create_board(self):
    """
    दिए गए बोर्ड आकार और आइकनों के साथ खेल का बोर्ड बनाएं
    :return: 2-आयामी सूची, खेल का बोर्ड
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
    
    # Create a flat list with pairs of icons
    # Each icon should appear an even number of times for matching
    tiles = []
    icons_count = len(self.icons)
    
    # Calculate how many of each icon we need
    # We need total_cells tiles, and each icon should appear in pairs
    tiles_per_icon = total_cells // icons_count
    
    # Create tiles with each icon appearing the required number of times
    for icon in self.icons:
        tiles.extend([icon] * tiles_per_icon)
    
    # If there are remaining cells, fill them with icons from the start
    remaining = total_cells - len(tiles)
    for i in range(remaining):
        tiles.append(self.icons[i % icons_count])
    
    # Shuffle the tiles
    random.shuffle(tiles)
    
    # Create the 2D board
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[i * cols + j])
        board.append(row)
    
    self.board = board
    return board