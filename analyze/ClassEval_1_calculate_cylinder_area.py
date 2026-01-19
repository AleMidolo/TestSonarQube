def calculate_cylinder_area(self, height):
    """
    calcola l'area del cilindro basata su self.radius e height
    :param height: altezza del cilindro, float
    :return: area del cilindro, float
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_cylinder_area(3)
    62.83185307179586
    """
    import math
    # Area del cilindro = 2πr² + 2πrh = 2πr(r + h)
    return 2 * math.pi * self.radius * (self.radius + height)