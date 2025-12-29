def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    self.postfix_stack.clear()
    arr = list(expression)
    current_number = ''
    i = 0
    while i < len(arr):
        c = arr[i]
        if c.isdigit() or c == '.' or c == '~':
            current_number += c
        else:
            if current_number:
                self.postfix_stack.append(current_number)
                current_number = ''
            if self.is_operator(c):
                if c == '(':
                    op_stack.append(c)
                elif c == ')':
                    while op_stack and op_stack[-1] != '(':
                        self.postfix_stack.append(op_stack.pop())
                    if op_stack:
                        op_stack.pop()
                else:
                    while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                        self.postfix_stack.append(op_stack.pop())
                    op_stack.append(c)
        i += 1
    if current_number:
        self.postfix_stack.append(current_number)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())