@staticmethod
def transform(expression):
    """
    Transformar la expresión en notación infija a un formato adecuado para la conversión
    :param expression: cadena, la expresión en notación infija a ser transformada
    :return: cadena, la expresión transformada
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.transform("2 + 3 * 4")
    "2+3*4"

    """
    return re.sub(r'\s+', '', expression)