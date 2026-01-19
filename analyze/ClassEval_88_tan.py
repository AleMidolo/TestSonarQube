def tan(self, x):
    """
        Calcular el valor de la tangente del ángulo en grados x
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    sin_val = self.sin(x)
    cos_val = self.cos(x)
    if fabs(cos_val) < 1e-10:
        raise ValueError('Tangent undefined for angle where cos(x) = 0')
    return round(sin_val / cos_val, 10)