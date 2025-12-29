def calculate_annulus_area(self, inner_radius, outer_radius):
    """
        calcola l'area dell'anello basata su inner_radius e outer_radius
        :param inner_radius: raggio interno del settore, float
        :param outer_radius: raggio esterno del settore, float
        :return: area dell'anello, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)