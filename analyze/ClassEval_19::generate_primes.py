def generate_primes(self):
    """
        Genera numeri primi fino al limite specificato utilizzando l'algoritmo del setaccio di Chandrasekhar.
        :return: lista, una lista di numeri primi
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]

        """
    if self.n < 2:
        return []
    is_prime = [True] * (self.n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, self.n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, self.n + 1, i):
                is_prime[j] = False
    return primes