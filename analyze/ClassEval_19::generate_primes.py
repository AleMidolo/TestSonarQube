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
    is_prime = [True] * ((self.n + 1) // 2)
    is_prime[0] = False
    limit = int(self.n ** 0.5)
    for i in range(1, (limit + 1) // 2):
        if is_prime[i]:
            p = 2 * i + 1
            start = p * p // 2
            step = p
            for j in range(start, len(is_prime), step):
                is_prime[j] = False
    primes = [2] if self.n >= 2 else []
    for i in range(1, len(is_prime)):
        if is_prime[i]:
            primes.append(2 * i + 1)
    return primes