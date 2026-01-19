def calculate_cylinder_area(self, height):
    """
        calcula el área del cilindro basado en self.radius y height
        :param height: altura del cilindro, float
        :return: área del cilindro, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
    return 2 * math.pi * self.radius * height + 2 * self.calculate_circle_area()