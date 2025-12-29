def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = 0
    while current_index < len(arr):
        c = arr[current_index]
        if c.isdigit():
            if count > 1:
                t = self.postfix_stack.pop() + c
                self.postfix_stack.append(t)
            else:
                self.postfix_stack.append(c)
            count += 1
        else:
            count = 0
            if c == ')':
                while op_stack:
                    op = op_stack.pop()
                    if op == '(':
                        break
                    else:
                        self.postfix_stack.append(op)
            elif not op_stack:
                op_stack.append(c)
            elif c == '(':
                op_stack.append(c)
            else:
                while op_stack:
                    op = op_stack[-1]
                    if op == '(':
                        break
                    elif self.compare(c, op):
                        self.postfix_stack.append(op_stack.pop())
                    else:
                        break
                op_stack.append(c)
        current_index += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())