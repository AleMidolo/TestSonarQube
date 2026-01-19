def calculate_annulus_area(self, inner_radius, outer_radius):
    """
        calculate the area of annulus based on inner_radius and out_radius
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of annulus, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)