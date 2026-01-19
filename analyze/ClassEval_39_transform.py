@staticmethod
def transform(expression):
    """
        将中缀表达式转换为适合转换的格式
        :param expression: 字符串，要转换的中缀表达式
        :return: 字符串，转换后的表达式
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
    expression = re.sub('\\s+', '', expression)
    transformed = []
    i = 0
    length = len(expression)
    while i < length:
        c = expression[i]
        if c == '-':
            if i == 0 or expression[i - 1] in {'+', '-', '*', '/', '(', '%'}:
                transformed.append('~')
            else:
                transformed.append(c)
        else:
            transformed.append(c)
        i += 1
    return ''.join(transformed)