def check_balanced_brackets(self):
    """
    Verifica si la expresión tiene paréntesis balanceados.
    :return: True si la expresión tiene paréntesis balanceados, False en caso contrario.
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