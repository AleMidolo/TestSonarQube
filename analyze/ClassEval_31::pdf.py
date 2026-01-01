@staticmethod
def pdf(data, mu, sigma):
    """
        Calcola la funzione di densità di probabilità (PDF) di un insieme di dati sotto una distribuzione normale.
        :param data: La lista di dati in ingresso, list.
        :param mu: La media della distribuzione normale, float.
        :param sigma: La deviazione standard della distribuzione normale, float.
        :return: La funzione di densità di probabilità (PDF), list.
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