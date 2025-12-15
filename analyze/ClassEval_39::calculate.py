def calculate(self, expression):
        """
        Calcola il risultato dell'espressione postfix fornita
        :param expression: stringa, l'espressione postfix da calcolare
        :return: float, il risultato calcolato
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