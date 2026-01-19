def clear_expr(self):
    """
    Clears the expression of all characters that are not brackets.
    >>> b = BalancedBrackets("a(b)c")
    >>> b.clear_expr()
    >>> b.expr
    '()'

    """
    brackets = {'(', ')', '[', ']', '{', '}'}
    self.expr = ''.join(char for char in self.expr if char in brackets)