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
    
    # Calculate how many pairs we need
    num_pairs = total_cells // 2
    
    # Create a flat list with pairs of icons
    flat_board = []
    icon_index = 0
    
    for _ in range(num_pairs):
        # Add a pair of the same icon
        flat_board.append(self.icons[icon_index % len(self.icons)])
        flat_board.append(self.icons[icon_index % len(self.icons)])
        icon_index += 1
    
    # If total_cells is odd, add one more icon
    if total_cells % 2 == 1:
        flat_board.append(self.icons[0])
    
    # Shuffle the flat board
    random.shuffle(flat_board)
    
    # Convert flat list to 2D board
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(flat_board[i * cols + j])
        board.append(row)
    
    self.board = board
    return board