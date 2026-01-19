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
        return eval(expression) == 24
    except Exception:
        return False