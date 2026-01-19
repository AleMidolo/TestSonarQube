@staticmethod
def transform(expression):
    """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
    expression = re.sub('\\s+', '', expression)
    result = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == '-':
            if i == 0 or expression[i - 1] in '+-*/(':
                result.append('~')
            else:
                result.append(c)
        else:
            result.append(c)
        i += 1
    return ''.join(result)