from math import pi, fabs


class TriCalculator:

    def __init__(self):
        pass

    def cos(self, x):
        return round(self.taylor(x, 50), 10)

    def factorial(self, a):
        return self._calculate_factorial(a)

    def taylor(self, x, n):
        x_rad = self._convert_to_radians(x)
        return self._calculate_taylor_series(x_rad, n)

    def sin(self, x):
        x_rad = self._convert_to_radians(x)
        return round(self._calculate_sine(x_rad), 10)

    def tan(self, x):
        cos_value = self.cos(x)
        if cos_value != 0:
            result = self.sin(x) / cos_value
            return round(result, 10)
        else:
            return False

    def _calculate_factorial(self, a):
        b = 1
        while a > 1:
            b *= a
            a -= 1
        return b

    def _convert_to_radians(self, x):
        return x / 180 * pi

    def _calculate_taylor_series(self, x, n):
        a = 1
        for k in range(1, n):
            term = (x ** (2 * k)) / self.factorial(2 * k)
            if k % 2 == 1:
                a -= term
            else:
                a += term
        return a

    def _calculate_sine(self, x):
        g = 0
        t = x
        n = 1

        while fabs(t) >= 1e-15:
            g += t
            n += 1
            t = -t * x * x / (2 * n - 1) / (2 * n - 2)
        return g