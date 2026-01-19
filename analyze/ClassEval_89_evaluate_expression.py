def evaluate_expression(self, expression):
    """
    评估一个数学表达式并检查结果是否为24。
    :param expression: 字符串，数学表达式
    :return: 布尔值，如果表达式的结果为24则返回True，否则返回False
    >>> game = TwentyFourPointGame()
    >>> nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.evaluate_expression(ans)
    True
    """
    try:
        # 评估表达式
        result = eval(expression)
        # 检查结果是否为24（考虑浮点数精度问题）
        return abs(result - 24) < 1e-6
    except:
        # 如果表达式无效，返回False
        return False