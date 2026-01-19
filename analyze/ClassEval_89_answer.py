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
    import re
    
    try:
        # Extract all numbers from the expression
        numbers_in_expr = re.findall(r'\d+', expression)
        numbers_in_expr = [int(num) for num in numbers_in_expr]
        
        # Check if the numbers used match the available numbers
        available_nums = sorted(self.nums)
        used_nums = sorted(numbers_in_expr)
        
        if available_nums != used_nums:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result is 24 (with floating point tolerance)
        return abs(result - 24) < 1e-9
        
    except:
        return False