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
        numbers = [num for num in numbers if num != p]
        i = 0
        while i < len(numbers):
            num = numbers[i]
            if num % p == 0:
                quotient = num // p
                if quotient % 2 != 0 and quotient % 3 != 0:
                    numbers.pop(i)
                else:
                    i += 1
            else:
                i += 1
    return primes