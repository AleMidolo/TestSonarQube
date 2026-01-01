def parse_more(self, i):
    """
        Analiza el sufijo de mil/millón/milmillón basado en el índice
        :param i: int, el índice que representa la magnitud (mil, millón, mil millones)
        :return: str, el sufijo correspondiente para la magnitud
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
    return self.NUMBER_MORE[i]