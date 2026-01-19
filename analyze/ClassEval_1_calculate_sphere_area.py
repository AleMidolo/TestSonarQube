def calculate_sphere_area(self):
    """
        calcula el área de la esfera basada en self.radius
        :return: área de la esfera, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
    return 4 * math.pi * self.radius ** 2