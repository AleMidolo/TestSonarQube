import math

def calculate_circle_area(self):
    """
    calcola l'area del cerchio basata su self.radius
    :return: area del cerchio, float
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_circle_area()
    12.566370614359172
    """
    return math.pi * self.radius ** 2