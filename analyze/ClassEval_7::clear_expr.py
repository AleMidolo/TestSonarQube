def clear_expr(self):
    """
        उन सभी कैरेक्टर के एक्सप्रेशन को क्लियर करता है जो ब्रैकेट नहीं हैं।

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
    filtered_chars = []
    for char in self.expr:
        if char in self.left_brackets or char in self.right_brackets:
            filtered_chars.append(char)
    self.expr = ''.join(filtered_chars)