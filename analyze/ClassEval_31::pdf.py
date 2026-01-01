@staticmethod
def pdf(data, mu, sigma):
    """
        计算在正态分布下的一组数据的概率密度函数 (PDF)。
        :param data: 输入数据列表，list。
        :param mu: 正态分布的均值，float。
        :param sigma: 正态分布的标准差，float。
        :return: 概率密度函数 (PDF)，list。
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]
        """
    return [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]