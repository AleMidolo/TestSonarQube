def check_balanced_brackets(self):
    """
    Checks if the expression has balanced brackets.
    :return: True if the expression has balanced brackets, False otherwise.
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = set(brackets.values())
    
    for char in self.expression:
        if char in brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0