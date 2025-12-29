def clear_expr(self):
    """
        清除表达式中所有不是括号的字符。
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
    cleaned = []
    for char in self.expr:
        if char in self.left_brackets or char in self.right_brackets:
            cleaned.append(char)
    self.expr = ''.join(cleaned)