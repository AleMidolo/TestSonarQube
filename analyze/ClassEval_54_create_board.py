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
    
    # Create a list of icons, repeating each icon twice to form pairs
    icons_list = []
    icon_index = 0
    for _ in range(num_pairs):
        icons_list.append(self.icons[icon_index % len(self.icons)])
        icons_list.append(self.icons[icon_index % len(self.icons)])
        icon_index += 1
    
    # Shuffle the icons
    random.shuffle(icons_list)
    
    # Create the 2D board
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icons_list[index])
            index += 1
        board.append(row)
    
    self.board = board
    return board