import math

@staticmethod
def pdf(data, mu, sigma):
    """
    सामान्य वितरण के तहत डेटा के एक सेट का संभाव्यता घनत्व फ़ंक्शन (PDF) की गणना करें।
    :param data: इनपुट डेटा सूची, सूची।
    :param mu: सामान्य वितरण का औसत, फ्लोट।
    :param sigma: सामान्य वितरण का मानक विचलन, फ्लोट।
    :return: संभाव्यता घनत्व फ़ंक्शन (PDF), सूची।
    >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
    [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

    """
    result = []
    for x in data:
        # Normal distribution PDF formula: (1 / (sigma * sqrt(2*pi))) * exp(-((x - mu)^2) / (2 * sigma^2))
        coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
        exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
        pdf_value = coefficient * math.exp(exponent)
        result.append(pdf_value)
    return result