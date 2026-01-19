def calculate_cylinder_area(self, height):
    """
    सिलेंडर का क्षेत्रफल self.radius और height के आधार पर गणना करें
    :param height: सिलेंडर की ऊँचाई, फ्लोट
    :return: सिलेंडर का क्षेत्रफल, फ्लोट
    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_cylinder_area(3)
    62.83185307179586
    """
    import math
    # Cylinder surface area = 2πr² + 2πrh = 2πr(r + h)
    return 2 * math.pi * self.radius * (self.radius + height)