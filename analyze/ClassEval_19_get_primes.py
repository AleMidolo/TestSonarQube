def get_primes(self):
    """
    获取生成的质数列表。
    :return: list, 一个质数列表
    >>> cs = ChandrasekharSieve(20)
    >>> cs.get_primes()
    [2, 3, 5, 7, 11, 13, 17, 19]

    """
    if not hasattr(self, 'primes'):
        self.primes = []
        if not hasattr(self, 'limit'):
            return self.primes
        
        if self.limit < 2:
            return self.primes
        
        # Sieve of Eratosthenes implementation
        is_prime = [True] * (self.limit + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(self.limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, self.limit + 1, i):
                    is_prime[j] = False
        
        self.primes = [i for i in range(2, self.limit + 1) if is_prime[i]]
    
    return self.primes