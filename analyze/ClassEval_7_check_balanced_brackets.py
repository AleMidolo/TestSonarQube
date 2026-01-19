def check_balanced_brackets(self):
    """
    जांचता है कि अभिव्यक्ति में संतुलित ब्रैकेट हैं या नहीं।
    :return: यदि अभिव्यक्ति में संतुलित ब्रैकेट हैं, तो True, अन्यथा False।
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in self.expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    
    return len(stack) == 0