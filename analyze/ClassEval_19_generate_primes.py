def generate_primes(self):
    """
    Genera numeri primi fino al limite specificato utilizzando l'algoritmo del setaccio di Chandrasekhar.
    :return: lista, una lista di numeri primi
    >>> cs = ChandrasekharSieve(20)
    >>> cs.generate_primes()
    [2, 3, 5, 7, 11, 13, 17, 19]

    """
    if self.limit < 2:
        return []
    
    # Create a boolean array "is_prime[0..limit]" and initialize all entries as true
    is_prime = [True] * (self.limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes (Chandrasekhar Sieve is a variant)
    p = 2
    while p * p <= self.limit:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, self.limit + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all numbers that are still marked as prime
    primes = [num for num in range(2, self.limit + 1) if is_prime[num]]
    
    return primes