class BalancedBrackets: 
    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True
        """
        self.clear_expr()
        for Brkt in self.expr:
            if Brkt in self.left_brackets:
                self.stack.append(Brkt)
            elif Brkt in self.right_brackets:
                if not self.stack:
                    return False
                Current_Brkt = self.stack.pop()
                if Current_Brkt == "(" and Brkt != ")":
                    return False
                if Current_Brkt == "{" and Brkt != "}":
                    return False
                if Current_Brkt == "[" and Brkt != "]":
                    return False
        return len(self.stack) == 0

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
        self.expr = ''.join([ch for ch in self.expr if ch in self.left_brackets + self.right_brackets])