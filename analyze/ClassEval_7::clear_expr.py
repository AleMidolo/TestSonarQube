def clear_expr(self):
    """
        Pulisce l'espressione da tutti i caratteri che non sono parentesi.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([char for char in self.expr if char in self.left_brackets + self.right_brackets])