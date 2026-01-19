def calculate(self, expression):
    """
    计算给定后缀表达式的结果
    :param expression: 字符串，要计算的后缀表达式
    :return: 浮点数，计算结果
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0

    """
    # First convert infix to postfix, then evaluate
    postfix = self._infix_to_postfix(expression)
    return self._evaluate_postfix(postfix)