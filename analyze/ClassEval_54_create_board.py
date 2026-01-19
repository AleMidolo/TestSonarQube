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
    
    # Calculate how many pairs we need
    num_pairs = total_cells // 2
    
    # Create a flat list with pairs of icons
    flat_board = []
    icon_index = 0
    for _ in range(num_pairs):
        icon = self.icons[icon_index % len(self.icons)]
        flat_board.extend([icon, icon])
        icon_index += 1
    
    # Shuffle the flat list
    random.shuffle(flat_board)
    
    # Convert to 2D board
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(flat_board[i * cols + j])
        board.append(row)
    
    self.board = board
    return board