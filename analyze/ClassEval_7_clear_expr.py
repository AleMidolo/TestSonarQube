def clear_expr(self):
    """
    Limpia la expresión de todos los caracteres que no son paréntesis.
    >>> b = BalancedBrackets("a(b)c")
    >>> b.clear_expr()
    >>> b.expr
    '()'

    """
    self.expr = ''.join(char for char in self.expr if char in '()[]{}')