def compare(self, cur, peek):
    """
        दो ऑपरेटरों की प्राथमिकता की तुलना करें
        :param cur: स्ट्रिंग, वर्तमान ऑपरेटर
        :param peek: स्ट्रिंग, ऑपरेटर स्टैक के शीर्ष पर मौजूद ऑपरेटर
        :return: बूल, यदि वर्तमान ऑपरेटर की प्राथमिकता उच्च या समान है, तो True, अन्यथा False
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
    if cur == '(':
        return False
    op_map = {'+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '%': 6, ',': 7}
    cur_idx = op_map.get(cur, -1)
    peek_idx = op_map.get(peek, -1)
    if cur_idx == -1 or peek_idx == -1:
        return False
    return self.operat_priority[cur_idx] <= self.operat_priority[peek_idx]