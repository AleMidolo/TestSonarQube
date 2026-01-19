def calculate_sector_area(self, angle):
    """
        calcula el área del sector basado en self.radius y el ángulo
        :param angle: ángulo del sector, float
        :return: área del sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
    return 0.5 * self.radius ** 2 * angle