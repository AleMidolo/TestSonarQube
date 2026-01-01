def generate_primes(self):
    """
        使用钱德拉塞卡筛法生成指定限制内的素数。
        :return: list, 一个素数列表
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
    if self.n < 2:
        return []
    sieve = [True] * (self.n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(self.n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, self.n + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]