def check_balanced_brackets(self):
    """
        Verifica si la expresión tiene paréntesis balanceados.
        :return: True si la expresión tiene paréntesis balanceados, False en caso contrario.
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
            top = self.stack.pop()
            left_index = self.left_brackets.index(top)
            right_index = self.right_brackets.index(char)
            if left_index != right_index:
                return False
    return len(self.stack) == 0