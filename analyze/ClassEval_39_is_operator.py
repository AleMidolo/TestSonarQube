@staticmethod
def is_operator(c):
    """
    Verifica si un carácter es un operador en {'+', '-', '*', '/', '(', ')', '%'}
    :param c: string, el carácter a verificar
    :return: bool, True si el carácter es un operador, False en caso contrario
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.is_operator("+")
    True

    """
    return c in {'+', '-', '*', '/', '(', ')', '%'}