def check_balanced_brackets(self):
    """
    Controlla se l'espressione ha parentesi bilanciate.
    :return: True se l'espressione ha parentesi bilanciate, False altrimenti.
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in self.expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0