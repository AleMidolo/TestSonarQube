def calculate(self, expression):
    """
        दिए गए एक्सप्रेशन की वैल्यू कैलकुलेट करें।

        :param expression: string, दिया गया एक्सप्रेशन
        :return: अगर सफल रहा, तो एक्सप्रेशन की वैल्यू रिटर्न करता है; नहीं तो None रिटर्न करता है

        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    if not expression:
        return None
    operand_stack = []
    operator_stack = []
    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]
        if char.isdigit() or char == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            try:
                num = float(expression[i:j])
            except ValueError:
                return None
            operand_stack.append(num)
            i = j
        elif char in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(char):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(char)
            i += 1
        elif char == '(':
            operator_stack.append(char)
            i += 1
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            if not operator_stack or operator_stack[-1] != '(':
                return None
            operator_stack.pop()
            i += 1
        elif char.isspace():
            i += 1
        else:
            return None
    while operator_stack:
        if operator_stack[-1] == '(':
            return None
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) == 1 and (not operator_stack):
        return operand_stack[0]
    else:
        return None