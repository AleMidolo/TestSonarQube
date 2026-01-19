def clear_expr(self):
    """
        उन सभी कैरेक्टर के एक्सप्रेशन को क्लियर करता है जो ब्रैकेट नहीं हैं।

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets or ch in self.right_brackets])