class ComplexCalculator:
    def __init__(self):
        pass

    @staticmethod
    def add(c1, c2):
        return ComplexCalculator._calculate(c1, c2, lambda r1, r2, i1, i2: (r1 + r2, i1 + i2))

    @staticmethod
    def subtract(c1, c2):
        return ComplexCalculator._calculate(c1, c2, lambda r1, r2, i1, i2: (r1 - r2, i1 - i2))

    @staticmethod
    def multiply(c1, c2):
        return ComplexCalculator._calculate(c1, c2, lambda r1, r2, i1, i2: (r1 * r2 - i1 * i2, r1 * i2 + i1 * r2))

    @staticmethod
    def divide(c1, c2):
        denominator = c2.real**2 + c2.imag**2
        return ComplexCalculator._calculate(c1, c2, lambda r1, r2, i1, i2: (
            (r1 * r2 + i1 * i2) / denominator,
            (i1 * r2 - r1 * i2) / denominator
        ))

    @staticmethod
    def _calculate(c1, c2, operation):
        real = operation(c1.real, c2.real, c1.imag, c2.imag)
        return complex(real[0], real[1])