class ComplexCalculator: 
    def __init__(self):
        pass

    def add(self, c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The sum of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)
        """
        real = c1.real + c2.real
        imaginary = c1.imag + c2.imag
        answer = complex(real, imaginary)
        return answer
    
    @staticmethod
    def multiply(c1, c2):
        """
            Multiplies two complex numbers.
            :param c1: The first complex number,complex.
            :param c2: The second complex number,complex.
            :return: The product of the two complex numbers,complex.
            >>> complexCalculator = ComplexCalculator()
            >>> complexCalculator.multiply(1+2j, 3+4j)
            (-5+10j)
        """
        real = c1.real * c2.real - c1.imag * c2.imag
        imaginary = c1.real * c2.imag + c1.imag * c2.real
        return complex(real, imaginary)
    
    @staticmethod
    def divide(c1, c2):
        """
            Divides two complex numbers.
            :param c1: The first complex number,complex.
            :param c2: The second complex number,complex.
            :return: The quotient of the two complex numbers,complex.
            >>> complexCalculator = ComplexCalculator()
            >>> complexCalculator.divide(1+2j, 3+4j)
            (0.44+0.08j)
        """
        denominator = c2.real**2 + c2.imag**2
        real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
        imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
        return complex(real, imaginary)
    
    @staticmethod
    def subtract(c1, c2):
        """
        दो जटिल संख्याओं को घटाता है।
        :param c1: पहली जटिल संख्या, complex.
        :param c2: दूसरी जटिल संख्या, complex.
        :return: दो जटिल संख्याओं का अंतर, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)
        """
        real = c1.real - c2.real
        imaginary = c1.imag - c2.imag
        return complex(real, imaginary)