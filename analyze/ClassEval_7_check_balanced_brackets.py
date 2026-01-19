def check_balanced_brackets(self):
    """
    जांचता है कि अभिव्यक्ति में संतुलित ब्रैकेट हैं या नहीं।
    :return: यदि अभिव्यक्ति में संतुलित ब्रैकेट हैं, तो True, अन्यथा False।
    >>> b = BalancedBrackets("a(b)c")
    >>> b.check_balanced_brackets()
    True

    """
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    closing_brackets = set(brackets.values())
    
    for char in self.expression:
        if char in brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0