def calculate_sphere_area(self):
    """
    self.radius के आधार पर गोले का एरिया कैलकुलेट करें।

    :return: sphereArea, float

    >>> areaCalculator = AreaCalculator(2)
    >>> areaCalculator.calculate_sphere_area()
    50.26548245743669
    """
    return 4 * math.pi * self.radius ** 2