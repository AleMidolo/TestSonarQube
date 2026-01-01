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
            elif arr[i - 1] == '+' or arr[i - 1] == '-' or arr[i - 1] == '*' or (arr[i - 1] == '/') or (arr[i - 1] == '(') or (arr[i - 1] == '%'):
                arr[i] = '~'
    if arr[0] == '~' and (len(arr) > 1 and arr[1] == '('):
        arr[0] = '-'
        return '0' + ''.join(arr)
    else:
        return ''.join(arr).replace('~', '-')