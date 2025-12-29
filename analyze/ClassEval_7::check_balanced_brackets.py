def check_balanced_brackets(self):
    """
        जांचता है कि अभिव्यक्ति में संतुलित ब्रैकेट हैं या नहीं।
        :return: यदि अभिव्यक्ति में संतुलित ब्रैकेट हैं, तो True, अन्यथा False।
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
    self.clear_expr()
    self.stack = []
    for char in self.expr:
        if char in self.left_brackets:
            self.stack.append(char)
        elif char in self.right_brackets:
            if not self.stack:
                return False
            left_bracket = self.stack.pop()
            left_index = self.left_brackets.index(left_bracket)
            right_index = self.right_brackets.index(char)
            if left_index != right_index:
                return False
    return len(self.stack) == 0