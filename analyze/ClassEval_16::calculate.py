def calculate(self, expression):
    """
        Calcola il valore di un'espressione data
        :param expression: stringa, espressione fornita
        :return: Se ha successo, restituisce il valore dell'espressione; altrimenti, restituisce None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    if not expression:
        return None
    expression = expression.replace(' ', '')
    if not expression:
        return None
    operand_stack = []
    operator_stack = []
    i = 0
    n = len(expression)
    while i < n:
        if expression[i].isdigit() or (expression[i] == '.' and i + 1 < n and expression[i + 1].isdigit()):
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
            if expression[i] == '-' and (i == 0 or expression[i - 1] in self.operators or expression[i - 1] == '('):
                j = i + 1
                if j < n and expression[j].isdigit():
                    while j < n and (expression[j].isdigit() or expression[j] == '.'):
                        j += 1
                    try:
                        num = -float(expression[i + 1:j])
                    except ValueError:
                        return None
                    operand_stack.append(num)
                    i = j
                    continue
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
        else:
            return None
    while operator_stack:
        if operator_stack[-1] == '(':
            return None
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) != 1 or operator_stack:
        return None
    return operand_stack[0]