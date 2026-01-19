def evaluate_expression(self, expression):
    """
        Evalúa una expresión matemática y verifica si el resultado es 24.
        :param expression: cadena, expresión matemática
        :return: bool, True si la expresión evalúa a 24, False en caso contrario
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        allowed_names = {'abs': abs, 'round': round, 'min': min, 'max': max, 'pow': pow, 'math': math}
        code = compile(expression, '<string>', 'eval')
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f'Use of {name} not allowed')
        result = eval(expression, {'__builtins__': {}}, allowed_names)
        return float(result)
    except:
        return float('inf')