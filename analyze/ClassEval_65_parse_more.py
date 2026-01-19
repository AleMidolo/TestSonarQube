def parse_more(self, i):
    """
    Analizza il suffisso di mille/milione/miliardo in base all'indice
    :param i: int, l'indice che rappresenta la grandezza (mille, milione, miliardo)
    :return: str, il suffisso corrispondente per la grandezza
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
    else:
        return ""