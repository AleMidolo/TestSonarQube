def clear_expr(self):
    """
        清除表达式中所有不是括号的字符。
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets + self.right_brackets])