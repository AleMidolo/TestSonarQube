def add(c1, c2):
        """
        दो जटिल संख्याओं को जोड़ता है।
        :param c1: पहली जटिल संख्या, complex.
        :param c2: दूसरी जटिल संख्या, complex.
        :return: दो जटिल संख्याओं का योग, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """
        return complex(c1.real + c2.real, c1.imag + c2.imag)