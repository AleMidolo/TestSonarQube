@staticmethod
def count_all(n):
    """
        Cuenta el número total de posibles arreglos al elegir al menos 1 artículo y como máximo n artículos de n artículos.
        :param n: int, el número total de artículos.
        :return: int, el conteo de todas las disposiciones.
        >>> ArrangementCalculator.count_all(4)
        64

        """
    return 2 ** n - 1