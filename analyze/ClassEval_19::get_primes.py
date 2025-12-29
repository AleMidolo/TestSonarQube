def get_primes(self):
    """
        获取生成的质数列表。
        :return: list, 一个质数列表
        >>> cs = ChandrasekharSieve(20)
        >>> cs.get_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
    return self.primes