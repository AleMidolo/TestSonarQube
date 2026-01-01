def calculate_sector_area(self, angle):
    """
        calcola l'area del settore basata su self.radius e angolo
        :param angle: angolo del settore, float
        :return: area del settore, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
    return angle / (2 * math.pi) * self.calculate_circle_area()