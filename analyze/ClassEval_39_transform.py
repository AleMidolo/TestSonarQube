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
    return re.sub(r'\s+', '', expression)