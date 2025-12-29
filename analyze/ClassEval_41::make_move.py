def make_move(self, row, col):
    """
        दिए गए पंक्ति और कॉलम पर एक चाल बनाता है।
        यदि चाल मान्य है, तो यह वर्तमान खिलाड़ी के प्रतीक को बोर्ड पर रखता है
        और वर्तमान खिलाड़ी को दूसरे खिलाड़ी में बदल देता है (यदि वर्तमान खिलाड़ी 'X' है, तो यह 'O' हो जाता है और इसके विपरीत)।
        :param row: int, इस चाल का पंक्ति अनुक्रमांक
        :param col: int, कॉलम अनुक्रमांक
        return: यदि चाल मान्य है तो True, अन्यथा False।
        >>> gomokuGame = GomokuGame(10)
        >>> gomokuGame.make_move(5, 5)
        True
        >>> gomokuGame.make_move(5, 5)
        False
        """
    if not (0 <= row < self.board_size and 0 <= col < self.board_size):
        return False
    if self.board[row][col] != ' ':
        return False
    self.board[row][col] = self.current_player
    self.current_player = 'O' if self.current_player == 'X' else 'X'
    return True