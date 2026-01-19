import math

def calculate_sector_area(self, angle):
    """
    self.radius और angle के आधार पर सेक्टर का एरिया कैलकुलेट करें।

    :param angle: सेक्टर का एंगल, float
    :return: सेक्टर का एरिया, float

    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_sector_area(math.pi)
    6.283185307179586
    """
    return 0.5 * self.radius ** 2 * angle