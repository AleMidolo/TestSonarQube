def evaluate_expression(self, expression):
    """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError('Division by zero')
            values.append(left / right)

    def evaluate(tokens):
        values = []
        operators = []
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit():
                j = i
                while j < len(tokens) and tokens[j].isdigit():
                    j += 1
                values.append(int(tokens[i:j]))
                i = j
            elif tokens[i] in '+-*/':
                while operators and operators[-1] in '+-*/' and (precedence[operators[-1]] >= precedence[tokens[i]]):
                    apply_operator(operators, values)
                operators.append(tokens[i])
                i += 1
            elif tokens[i] == '(':
                operators.append(tokens[i])
                i += 1
            elif tokens[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
                i += 1
            else:
                i += 1
        while operators:
            apply_operator(operators, values)
        return values[0] if values else 0
    try:
        result = evaluate(expression)
        return result
    except:
        raise ValueError('Invalid expression')