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
    if not expression:
        return expression
    expression = re.sub('\\s+', '', expression)
    arr = list(expression)
    for i in range(len(arr)):
        if arr[i] == '-':
            if i == 0:
                arr[i] = '~'
            elif arr[i - 1] in {'+', '-', '*', '/', '(', '%'}:
                arr[i] = '~'
    return ''.join(arr)