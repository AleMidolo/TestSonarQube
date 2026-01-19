@staticmethod
def transform(expression):
    """
    Trasforma l'espressione in notazione infissa in un formato adatto per la conversione
    :param expression: stringa, l'espressione infissa da trasformare
    :return: stringa, l'espressione trasformata
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.transform("2 + 3 * 4")
    "2+3*4"

    """
    return re.sub(r'\s+', '', expression)