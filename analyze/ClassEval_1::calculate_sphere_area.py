def calculate_sphere_area(self):
    """
        calcola l'area della sfera basata su self.radius
        :return: area della sfera, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
    return 4 * math.pi * self.radius ** 2