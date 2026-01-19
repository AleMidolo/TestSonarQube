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
    rows, cols = self.BOARD_SIZE
    total_cells = rows * cols
    icon_count = len(self.ICONS)
    icons_list = []
    for i in range(total_cells // 2):
        icons_list.append(self.ICONS[i % icon_count])
        icons_list.append(self.ICONS[i % icon_count])
    if total_cells % 2 == 1:
        icons_list.append(random.choice(self.ICONS))
    random.shuffle(icons_list)
    board = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(icons_list[index])
            index += 1
        board.append(row)
    return board