def clear_expr(self):
    """
        Pulisce l'espressione da tutti i caratteri che non sono parentesi.
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