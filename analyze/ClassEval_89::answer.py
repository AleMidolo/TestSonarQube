def answer(self, expression):
    """
    检查给定的数学表达式是否可以使用这些牌计算出24。
    :param expression: 字符串，使用牌的数学表达式
    :return: 布尔值，如果表达式计算结果为24则返回True，否则返回False
    >>> game = TwentyFourPointGame()
    >>> game.nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.answer(ans)
    True
    """
    
    return self.evaluate_expression(expression)