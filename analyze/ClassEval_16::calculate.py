def calculate(self, expression):
    """
    दिए गए एक्सप्रेशन की वैल्यू कैलकुलेट करें।

    :param expression: string, दिया गया एक्सप्रेशन
    :return: अगर सफल रहा, तो एक्सप्रेशन की वैल्यू रिटर्न करता है; नहीं तो None रिटर्न करता है

    >>> calculator = Calculator()
    >>> calculator.calculate('1+2-3')
    0.0
    """
    operand_stack = []
    operator_stack = []
    i = 0
    n = len(expression)

    while i < n:
        if expression[i].isdigit():
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operand_stack.append(num)
            continue
        elif expression[i] in self.operators:
            while (operator_stack and 
                   self.precedence(operator_stack[-1]) >= self.precedence(expression[i])):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(expression[i])
        i += 1

    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)

    return operand_stack[0] if operand_stack else None