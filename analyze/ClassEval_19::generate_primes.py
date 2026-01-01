def generate_primes(self):
    """
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]

        """
    if self.n < 2:
        return []
    numbers = list(range(2, self.n + 1))
    primes = []
    while numbers:
        p = numbers[0]
        primes.append(p)
        numbers = [x for x in numbers if x % p != 0]
    return primes