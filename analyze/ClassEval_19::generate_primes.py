def generate_primes(self):
    """
        निर्दिष्ट सीमा तक चंद्रशेखर छानने के एल्गोरिदम का उपयोग करके अभाज्य संख्याएँ उत्पन्न करें।
        :return: सूची, अभाज्य संख्याओं की एक सूची
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
    sieve = [True] * (self.n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(self.n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, self.n + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]