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
    tiles = []
    icon_index = 0
    
    # We need total_cells tiles, and each icon should appear in pairs
    for i in range(total_cells):
        tiles.append(self.icons[icon_index % len(self.icons)])
        icon_index += 1
    
    # Shuffle the tiles
    random.shuffle(tiles)
    
    # Create 2D board from flat list
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(tiles[i * cols + j])
        board.append(row)
    
    self.board = board
    return board