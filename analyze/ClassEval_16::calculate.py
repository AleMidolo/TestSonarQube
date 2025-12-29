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
                operand_stack.append(float(expression[i:j]))
            except ValueError:
                return None
            i = j
        elif expression[i] in self.operators:
            if expression[i] == '-' and (i == 0 or expression[i - 1] in self.operators or expression[i - 1] == '('):
                j = i + 1
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                try:
                    operand_stack.append(-float(expression[i + 1:j]))
                except ValueError:
                    return None
                i = j
            else:
                while operator_stack and operator_stack[-1] != '(' and (self.precedence(operator_stack[-1]) >= self.precedence(expression[i])):
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
                i += 1
        elif expression[i] == '(':
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operator_stack and operator_stack[-1] != '(':
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            if not operator_stack or operator_stack[-1] != '(':
                return None
            operator_stack.pop()
            i += 1
        elif expression[i].isspace():
            i += 1
        else:
            return None
    while operator_stack:
        if operator_stack[-1] == '(':
            return None
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) != 1 or operator_stack:
        return None
    return operand_stack[0]