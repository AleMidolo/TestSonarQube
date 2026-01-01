def clear_expr(self):
    """
        Removes all characters from the expression that are not brackets.

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets or ch in self.right_brackets])