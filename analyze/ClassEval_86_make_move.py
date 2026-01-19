def make_move(self, row, col):
    """
        वर्तमान खिलाड़ी का निशान निर्दिष्ट स्थिति पर बोर्ड पर रखें और निशान को बदलें।
        :param row: int, स्थिति का पंक्ति अनुक्रमांक
        :param col: int, स्थिति का कॉलम अनुक्रमांक
        :return: bool, यह दर्शाता है कि चाल सफल थी या नहीं
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
    if row < 0 or row >= 3 or col < 0 or (col >= 3):
        return False
    if self.board[row][col] != ' ':
        return False
    self.board[row][col] = self.current_player
    self.current_player = 'O' if self.current_player == 'X' else 'X'
    return True