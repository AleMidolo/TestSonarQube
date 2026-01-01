def precedence(self, operator):
    """
        निर्दिष्ट ऑपरेटर की प्राथमिकता लौटाता है, जहाँ उच्च प्राथमिकता का अर्थ है अधिक असाइनमेंट। '^' की प्राथमिकता '/' और '*' से अधिक है, और '/' और '*' की प्राथमिकता '+' और '-' से अधिक है।
        :param operator: स्ट्रिंग, दिया गया ऑपरेटर
        :return: int, दिए गए ऑपरेटर की प्राथमिकता, अन्यथा 0 लौटाएं
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
    if operator == '^':
        return 3
    elif operator in '*/':
        return 2
    elif operator in '+-':
        return 1
    return 0