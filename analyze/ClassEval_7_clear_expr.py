def clear_expr(self):
    """
    उन सभी कैरेक्टर के एक्सप्रेशन को क्लियर करता है जो ब्रैकेट नहीं हैं।

    >>> b = BalancedBrackets("a(b)c")
    >>> b.clear_expr()
    >>> b.expr
    '()'
    """
    self.expr = ''.join(char for char in self.expr if char in '()[]{}')