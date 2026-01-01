def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    output = []
    operator_stack = []
    for char in expression:
        if char.isdigit() or char == '~':
            output.append(char)
        elif self.is_operator(char):
            while operator_stack and operator_stack[-1] != '(' and self.compare(char, operator_stack[-1]):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        output.append(operator_stack.pop())
    self.postfix_stack = output