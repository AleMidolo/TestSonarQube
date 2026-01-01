@staticmethod
def pdf(data, mu, sigma):
    """
        Calcular la función de densidad de probabilidad (PDF) de un conjunto de datos bajo una distribución normal.
        :param data: La lista de datos de entrada, lista.
        :param mu: La media de la distribución normal, float.
        :param sigma: La desviación estándar de la distribución normal, float.
        :return: La función de densidad de probabilidad (PDF), lista.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

        """
    if sigma <= 0:
        raise ValueError('Sigma must be positive')
    pdf_values = []
    constant = 1 / (sigma * math.sqrt(2 * math.pi))
    for x in data:
        exponent = -(x - mu) ** 2 / (2 * sigma ** 2)
        pdf_value = constant * math.exp(exponent)
        pdf_values.append(pdf_value)
    return pdf_values