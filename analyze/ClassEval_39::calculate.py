def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        self.postfix_stack.clear()
        expression = self.transform(expression)
        self.prepare(expression)
        
        op_stack = deque()
        
        for token in self.postfix_stack:
            if not self.is_operator(token):
                op_stack.append(token)
            else:
                second_value = op_stack.pop()
                first_value = op_stack.pop()
                result = self._calculate(first_value, second_value, token)
                op_stack.append(result)
        
        return float(op_stack.pop())