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
    try:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        tokens = []
        current = ''
        for char in expression:
            if char.isdigit():
                current += char
            else:
                if current:
                    tokens.append(int(current))
                    current = ''
                if char in ops:
                    tokens.append(char)
        if current:
            tokens.append(int(current))

        def evaluate(tokens):
            i = 0
            while i < len(tokens):
                if tokens[i] == '*':
                    left = tokens[i - 1]
                    right = tokens[i + 1]
                    result = ops['*'](left, right)
                    tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
                    i -= 1
                elif tokens[i] == '/':
                    left = tokens[i - 1]
                    right = tokens[i + 1]
                    if right == 0:
                        return None
                    result = ops['/'](left, right)
                    tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
                    i -= 1
                else:
                    i += 1
            result = tokens[0]
            i = 1
            while i < len(tokens):
                if tokens[i] == '+':
                    result = ops['+'](result, tokens[i + 1])
                elif tokens[i] == '-':
                    result = ops['-'](result, tokens[i + 1])
                i += 2
            return result
        result = evaluate(tokens)
        if result is None:
            return False
        return abs(result - 24) < 1e-10
    except (IndexError, ZeroDivisionError, ValueError, TypeError):
        return False