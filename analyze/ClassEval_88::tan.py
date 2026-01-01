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
    if abs(cos_val) < 1e-10:
        raise ValueError(f'Tangent is undefined for angle {x} degrees (cos({x}) = 0)')
    tan_val = sin_val / cos_val
    return round(tan_val, 10)