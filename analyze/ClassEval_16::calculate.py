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
        if expression[i].isdigit() or expression[i] == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            try:
                num = float(expression[i:j])
            except ValueError:
                return None
            operand_stack.append(num)
            i = j
        elif expression[i] in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i]):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            i += 1
        else:
            return None
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) == 1:
        return operand_stack[0]
    else:
        return None