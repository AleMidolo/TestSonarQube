def parse_more(self, i):
    """
    Analizza il suffisso di mille/milione/miliardo in base all'indice
    :param i: int, l'indice che rappresenta la grandezza (mille, milione, miliardo)
    :return: str, il suffisso corrispondente per la grandezza
    >>> formatter = NumberWordFormatter()
    >>> formatter.parse_more(1)
    "THOUSAND"
    """
    suffixes = {
        1: "THOUSAND",
        2: "MILLION",
        3: "BILLION"
    }
    return suffixes.get(i, "")