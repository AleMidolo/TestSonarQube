def check_balanced_brackets(self):
    """
    Checks if the expression has balanced brackets.
    :return: True if the expression has balanced brackets, False otherwise.
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    opening_brackets = set(bracket_pairs.keys())
    closing_brackets = set(bracket_pairs.values())
    
    for char in self.expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening = stack.pop()
            if bracket_pairs[last_opening] != char:
                return False
    
    return len(stack) == 0