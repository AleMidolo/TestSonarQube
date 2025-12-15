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
    
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x / 180 * pi
        g = 0
        t = x
        n = 1
    
        while fabs(t) >= 1e-15:
            g += t
            n += 1
            t = -t * x * x / (2 * n - 1) / (2 * n - 2)
        return round(g, 10)
    
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
    
    def taylor(self, x, n):
        """
        cos (x/180 * pi) का n-आदेश टेलर विस्तार मान खोजें
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        x = x / 180 * pi
        cos_value = 0
        for i in range(n):
            cos_value += ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
        return cos_value