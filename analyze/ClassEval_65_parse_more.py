def parse_more(self, i):
    """
    Analiza el sufijo de mil/millón/milmillón basado en el índice
    :param i: int, el índice que representa la magnitud (mil, millón, mil millones)
    :return: str, el sufijo correspondiente para la magnitud
    >>> formatter = NumberWordFormatter()
    >>> formatter.parse_more(1)
    "THOUSAND"
    """
    if i == 1:
        return "THOUSAND"
    elif i == 2:
        return "MILLION"
    elif i == 3:
        return "BILLION"
    elif i == 4:
        return "TRILLION"
    elif i == 5:
        return "QUADRILLION"
    elif i == 6:
        return "QUINTILLION"
    else:
        return ""