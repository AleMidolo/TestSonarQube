def answer(self, expression):
    """
    Controlla se una data espressione matematica usando le carte può valutarsi a 24.
    :param expression: stringa, espressione matematica usando le carte
    :return: bool, True se l'espressione si valuta a 24, False altrimenti
    >>> game = TwentyFourPointGame()
    >>> game.nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.answer(ans)
    True
    """
    import re
    
    # Estrai tutti i numeri dall'espressione
    numbers_in_expr = re.findall(r'\d+', expression)
    numbers_in_expr = [int(n) for n in numbers_in_expr]
    
    # Verifica che i numeri usati corrispondano esattamente alle carte disponibili
    sorted_nums = sorted(self.nums)
    sorted_expr_nums = sorted(numbers_in_expr)
    
    if sorted_nums != sorted_expr_nums:
        return False
    
    # Valuta l'espressione
    try:
        result = eval(expression)
        # Verifica se il risultato è 24 (con tolleranza per errori di floating point)
        return abs(result - 24) < 1e-9
    except:
        return False