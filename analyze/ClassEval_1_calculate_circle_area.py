import math

def calculate_circle_area(self):
    """
    根据self.radius计算圆的面积
    :return: 圆的面积，浮点数
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_circle_area()
    12.566370614359172
    """
    return math.pi * self.radius ** 2