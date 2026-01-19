import math

def calculate_circle_area(self):
    """
    self.radius के आधार पर वृत्त का क्षेत्रफल निकालें
    :return: वृत्त का क्षेत्रफल, float
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_circle_area()
    12.566370614359172
    """
    return math.pi * self.radius ** 2