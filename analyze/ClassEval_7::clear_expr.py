def clear_expr(self):
    """
        Clears the expression of all characters that are not brackets.

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets + self.right_brackets])