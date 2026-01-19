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
    # Define operator precedence levels
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
        '**': 3
    }
    
    # Get precedence of current and peek operators
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # Return True if current operator has higher or equal precedence
    return cur_precedence >= peek_precedence