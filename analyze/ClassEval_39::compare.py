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
    operators = {'+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '%': 6, ',': 7}
    cur_index = operators.get(cur, -1)
    peek_index = operators.get(peek, -1)
    if cur_index >= 0 and peek_index >= 0 and (cur_index < len(self.operat_priority)) and (peek_index < len(self.operat_priority)):
        return self.operat_priority[cur_index] <= self.operat_priority[peek_index]
    return False