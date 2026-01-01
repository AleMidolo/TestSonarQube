def generate_primes(self):
    """
        Generar números primos hasta el límite especificado utilizando el algoritmo de la criba de Chandrasekhar.
        :return: lista, una lista de números primos
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]

        """
    if self.n < 2:
        return []
    is_prime = [True] * (self.n + 1)
    is_prime[0] = is_prime[1] = False
    if self.n >= 2:
        for i in range(4, self.n + 1, 2):
            is_prime[i] = False
    p = 3
    while p * p <= self.n:
        if is_prime[p]:
            for i in range(p * p, self.n + 1, 2 * p):
                is_prime[i] = False
        p += 2
    primes = []
    for i in range(2, self.n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes