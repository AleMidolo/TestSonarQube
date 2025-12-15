from math import pi, fabs

class TriCalculator: 
    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        return round(self.taylor(x, 50), 10)
    
    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        b = 1
        while a != 1:
            b *= a
            a -= 1
        return b
    
    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        a = 1
        x = x / 180 * pi
        count = 1
        for k in range(1, n):
            if count % 2 != 0:
                a -= (x ** (2 * k)) / self.factorial(2 * k)
            else:
                a += (x ** (2 * k)) / self.factorial(2 * k)
            count += 1
        return a
    
    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        if self.cos(x) != 0:
            result = self.sin(x) / self.cos(x)
            return round(result, 10)
        else:
            return False
    
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x / 180 * pi
        return round(self.taylor_sin(x, 50), 10)

    def taylor_sin(self, x, n):
        """
        Finding the n-order Taylor expansion value of sin (x)
        :param x: float
        :param n: int
        :return: float
        >>> tricalculator.taylor_sin(pi/6, 50)
        0.49999999999999994
        """
        a = 0
        for k in range(n):
            a += ((-1) ** k) * (x ** (2 * k + 1)) / self.factorial(2 * k + 1)
        return a