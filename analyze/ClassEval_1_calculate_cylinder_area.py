def calculate_cylinder_area(self, height):
    """
    calcula el área del cilindro basado en self.radius y height
    :param height: altura del cilindro, float
    :return: área del cilindro, float
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_cylinder_area(3)
    62.83185307179586
    """
    import math
    # Área del cilindro = 2πr² + 2πrh = 2πr(r + h)
    return 2 * math.pi * self.radius * (self.radius + height)