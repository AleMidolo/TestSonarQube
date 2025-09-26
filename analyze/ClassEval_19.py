class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        if self.n < 2:
            return []

        sieve = self.initialize_sieve()
        self.populate_sieve(sieve)

        return self.extract_primes(sieve)

    def initialize_sieve(self):
        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False
        return sieve

    def populate_sieve(self, sieve):
        p = 2
        while p * p <= self.n:
            if sieve[p]:
                for i in range(p * p, self.n + 1, p):
                    sieve[i] = False
            p += 1

    def extract_primes(self, sieve):
        return [i for i in range(2, self.n + 1) if sieve[i]]

    def get_primes(self):
        return self.primes