from math import pi, fabs


class TriCalculator:

    MAX_ITERATIONS = 50
    EPSILON = 1e-15

    def __init__(self):
        pass

    def cos(self, x):
        return round(self.taylor(x, self.MAX_ITERATIONS), 10)

    def factorial(self, a):
        if a == 0 or a == 1:
            return 1
        b = 1
        for i in range(2, a + 1):
            b *= i
        return b

    def taylor(self, x, n):
        x_rad = self.to_radians(x)
        result = 1
        for k in range(1, n):
            term = (x_rad ** (2 * k)) / self.factorial(2 * k)
            result += term if k % 2 == 0 else -term
        return result

    def sin(self, x):
        x_rad = self.to_radians(x)
        g = 0
        t = x_rad
        n = 1

        while fabs(t) >= self.EPSILON:
            g += t
            n += 1
            t = -t * x_rad * x_rad / (2 * n - 1) / (2 * n - 2)
        return round(g, 10)

    def tan(self, x):
        cos_value = self.cos(x)
        if cos_value != 0:
            result = self.sin(x) / cos_value
            return round(result, 10)
        else:
            return False

    def to_radians(self, degrees):
        return degrees / 180 * pi