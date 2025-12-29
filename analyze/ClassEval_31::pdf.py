@staticmethod
def pdf(data, mu, sigma):
    """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]
        """
    if sigma <= 0:
        raise ValueError('Standard deviation must be positive')
    pdf_values = []
    constant = 1 / (sigma * math.sqrt(2 * math.pi))
    for x in data:
        exponent = -(x - mu) ** 2 / (2 * sigma ** 2)
        pdf_val = constant * math.exp(exponent)
        pdf_values.append(pdf_val)
    return pdf_values