def answer(self, expression):
    """
    Verifica si una expresión matemática dada utilizando las cartas puede evaluarse a 24.
    :param expression: cadena, expresión matemática utilizando las cartas
    :return: bool, True si la expresión se evalúa a 24, False en caso contrario
    >>> game = TwentyFourPointGame()
    >>> game.nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.answer(ans)
    True
    """
    import re
    
    # Extraer todos los números de la expresión
    numbers_in_expr = re.findall(r'\d+', expression)
    numbers_in_expr = [int(num) for num in numbers_in_expr]
    
    # Verificar que se usen exactamente los mismos números que en self.nums
    sorted_nums = sorted(self.nums)
    sorted_expr_nums = sorted(numbers_in_expr)
    
    if sorted_nums != sorted_expr_nums:
        return False
    
    # Evaluar la expresión y verificar si es igual a 24
    try:
        result = eval(expression)
        # Usar una pequeña tolerancia para comparación de punto flotante
        return abs(result - 24) < 1e-9
    except:
        return False