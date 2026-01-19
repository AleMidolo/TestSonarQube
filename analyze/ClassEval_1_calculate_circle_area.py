import math

def calculate_circle_area(self):
    """
    calcula el área del círculo basado en self.radius
    :return: área del círculo, float
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_circle_area()
    12.566370614359172
    """
    return math.pi * self.radius ** 2