def calculate_annulus_area(self, inner_radius, outer_radius):
    """
        calcula el área del anillo basado en inner_radius y outer_radius
        :param inner_radius: radio interno del sector, float
        :param outer_radius: radio externo del sector, float
        :return: área del anillo, float
        >>> areaCalculator = AreaCalculator(0)  # radius is not used in this method
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)