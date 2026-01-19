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
    try:
        # Extract numbers from the expression
        import re
        numbers_in_expr = []
        for char in expression:
            if char.isdigit():
                numbers_in_expr.append(int(char))
        
        # Sort both lists to compare
        numbers_in_expr_sorted = sorted(numbers_in_expr)
        nums_sorted = sorted(self.nums)
        
        # Check if the numbers used match the available numbers
        if numbers_in_expr_sorted != nums_sorted:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24 (with floating point tolerance)
        return abs(result - 24) < 1e-9
    except:
        return False