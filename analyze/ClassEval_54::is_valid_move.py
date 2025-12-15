def is_valid_move(self, pos1, pos2):
        """
        दो आइकनों की चाल को मान्य है या नहीं, यह जांचें (यानी, स्थान खेल बोर्ड की सीमा के भीतर हैं, दोनों स्थान समान नहीं हैं, दोनों स्थानों में समान आइकन हैं, और दोनों स्थानों के बीच एक मान्य पथ है)
        :param pos1: पहले आइकन की स्थिति ट्यूपल(x, y)
        :param pos2: दूसरे आइकन की स्थिति ट्यूपल(x, y)
        :return: True या False, जो दर्शाता है कि दो आइकनों की चाल मान्य है या नहीं
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        if pos1 == pos2:
            return False
        
        x1, y1 = pos1
        x2, y2 = pos2
        
        if not (0 <= x1 < self.BOARD_SIZE[0] and 0 <= y1 < self.BOARD_SIZE[1]):
            return False
        if not (0 <= x2 < self.BOARD_SIZE[0] and 0 <= y2 < self.BOARD_SIZE[1]):
            return False
        
        if self.board[x1][y1] != self.board[x2][y2]:
            return False
        
        return self.has_path(pos1, pos2)