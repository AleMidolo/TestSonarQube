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
        if self.limit < 2:
            return self.primes
        
        # Create a boolean array "is_prime[0..limit]" and initialize
        # all entries as true
        is_prime = [True] * (self.limit + 1)
        is_prime[0] = is_prime[1] = False
        
        # Sieve of Eratosthenes
        p = 2
        while p * p <= self.limit:
            if is_prime[p]:
                # Mark all multiples of p as not prime
                for i in range(p * p, self.limit + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Collect all prime numbers
        self.primes = [i for i in range(2, self.limit + 1) if is_prime[i]]
    
    return self.primes