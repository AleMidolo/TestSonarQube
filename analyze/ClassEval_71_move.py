def move(self, direction):
    """
        निर्दिष्ट दिशा के आधार पर खिलाड़ी को स्थानांतरित करें और जांचें कि खेल जीता गया है या नहीं।
        :param direction: str, खिलाड़ी की गति की दिशा। 
            यह 'w', 's', 'a', या 'd' हो सकता है जो क्रमशः ऊपर, नीचे, बाएं, या दाएं का प्रतिनिधित्व करता है।

        :return: यदि खेल जीता गया है तो True, अन्यथा False।
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
    if self.is_game_over:
        return True
    dir_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if direction not in dir_map:
        return False
    dr, dc = dir_map[direction]
    new_row = self.player_row + dr
    new_col = self.player_col + dc
    if new_row < 0 or new_row >= len(self.map) or new_col < 0 or (new_col >= len(self.map[0])):
        return False
    if self.map[new_row][new_col] == '#':
        return False
    box_index = -1
    for i, box in enumerate(self.boxes):
        if box == (new_row, new_col):
            box_index = i
            break
    if box_index != -1:
        box_new_row = new_row + dr
        box_new_col = new_col + dc
        if box_new_row < 0 or box_new_row >= len(self.map) or box_new_col < 0 or (box_new_col >= len(self.map[0])) or (self.map[box_new_row][box_new_col] == '#') or ((box_new_row, box_new_col) in self.boxes):
            return False
        self.boxes[box_index] = (box_new_row, box_new_col)
    self.player_row = new_row
    self.player_col = new_col
    return self.check_win()