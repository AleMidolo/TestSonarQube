import math

def calculate_sector_area(self, angle):
    """
    根据 self.radius 和角度计算扇形的面积
    :param angle: 扇形的角度，浮点数
    :return: 扇形的面积，浮点数
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_sector_area(math.pi)
    6.283185307179586
    """
    return 0.5 * self.radius ** 2 * angle