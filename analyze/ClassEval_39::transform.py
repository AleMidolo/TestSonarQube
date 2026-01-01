@staticmethod
def transform(expression):
    """
        इनफिक्स अभिव्यक्ति को रूपांतरित करने के लिए उपयुक्त प्रारूप में बदलें
        :param expression: स्ट्रिंग, रूपांतरित की जाने वाली इनफिक्स अभिव्यक्ति
        :return: स्ट्रिंग, रूपांतरित अभिव्यक्ति
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
    expression = re.sub('\\s+', '', expression)
    transformed = []
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char == '-':
            if i == 0:
                transformed.append('~')
            elif expression[i - 1] in '+-*/%(' or expression[i - 1] == '~':
                transformed.append('~')
            else:
                transformed.append(char)
        else:
            transformed.append(char)
        i += 1
    return ''.join(transformed)