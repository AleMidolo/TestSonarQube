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
        real = c1.real * c2.real - c1.imag * c2.imag
        imaginary = c1.real * c2.imag + c1.imag * c2.real
        return complex(real, imaginary)

    @staticmethod
    def divide(c1, c2):
        denominator = c2.real**2 + c2.imag**2
        real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
        imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
        return complex(real, imaginary)

    @staticmethod
    def _calculate(c1, c2, operation):
        real_result, imaginary_result = operation(c1.real, c2.real, c1.imag, c2.imag)
        return complex(real_result, imaginary_result)