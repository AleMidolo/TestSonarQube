@staticmethod
def is_operator(c):
    """
    Controlla se un carattere è un operatore in {'+', '-', '*', '/', '(', ')', '%'}
    :param c: stringa, il carattere da controllare
    :return: bool, True se il carattere è un operatore, False altrimenti
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.is_operator("+")
    True

    """
    return c in {'+', '-', '*', '\/', '(', ')', '%'}