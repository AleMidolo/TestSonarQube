class BalancedBrackets:
    LEFT_BRACKETS = ["(", "{", "["]
    RIGHT_BRACKETS = [")", "}", "]"]

    def __init__(self, expr):
        self.stack = []
        self.expr = expr

    def clear_expr(self):
        self.expr = ''.join(c for c in self.expr if self.is_bracket(c))

    def is_bracket(self, char):
        return char in self.LEFT_BRACKETS or char in self.RIGHT_BRACKETS

    def check_balanced_brackets(self):
        self.clear_expr()
        for bracket in self.expr:
            if bracket in self.LEFT_BRACKETS:
                self.stack.append(bracket)
            else:
                if not self.is_matching_bracket(self.stack.pop(), bracket):
                    return False
        return not self.stack

    def is_matching_bracket(self, left_bracket, right_bracket):
        return (left_bracket == "(" and right_bracket == ")") or \
               (left_bracket == "{" and right_bracket == "}") or \
               (left_bracket == "[" and right_bracket == "]")