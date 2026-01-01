def clear_expr(self):
    """
        Limpia la expresión de todos los caracteres que no son paréntesis.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets + self.right_brackets])