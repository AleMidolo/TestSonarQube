def calculate_annulus_area(self, inner_radius, outer_radius):
    """
        计算环形区域的面积，基于内半径和外半径
        :param inner_radius: 扇形的内半径，浮点数
        :param outer_radius: 扇形的外半径，浮点数
        :return: 环形区域的面积，浮点数
        >>> areaCalculator = AreaCalculator(0)  # radius is not used in this method
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)