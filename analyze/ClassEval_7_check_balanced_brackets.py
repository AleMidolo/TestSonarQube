def check_balanced_brackets(self):
    """
    检查表达式是否有平衡的括号。
    :return: 如果表达式有平衡的括号则返回 True，否则返回 False。
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in self.expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return len(stack) == 0