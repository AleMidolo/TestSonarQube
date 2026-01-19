def clear_expr(self):
    """
        Clears the expression of all characters that are not brackets.
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