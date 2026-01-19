@staticmethod
def is_operator(c):
    """
    检查一个字符是否是 {'+', '-', '*', '/', '(', ')', '%'} 中的运算符
    :param c: 字符串，要检查的字符
    :return: 布尔值，如果字符是运算符则返回 True，否则返回 False
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.is_operator("+")
    True

    """
    return c in {'+', '-', '*', '/', '(', ')', '%'}