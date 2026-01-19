def clear_expr(self):
    """
    清除表达式中所有不是括号的字符。
    >>> b = BalancedBrackets("a(b)c")
    >>> b.clear_expr()
    >>> b.expr
    '()'

    """
    brackets = {'(', ')', '[', ']', '{', '}'}
    self.expr = ''.join(char for char in self.expr if char in brackets)