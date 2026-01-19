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
    try:
        # Extraer los números de la expresión
        import re
        nums_in_expr = re.findall(r'\d+', expression)
        nums_in_expr = [int(num) for num in nums_in_expr]
        
        # Verificar que se usen exactamente los mismos números que en self.nums
        if sorted(nums_in_expr) != sorted(self.nums):
            return False
        
        # Evaluar la expresión
        result = eval(expression)
        
        # Verificar si el resultado es 24 (con tolerancia para errores de punto flotante)
        return abs(result - 24) < 1e-6
    except:
        return False