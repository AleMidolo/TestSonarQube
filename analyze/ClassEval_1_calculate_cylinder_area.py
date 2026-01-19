def calculate_cylinder_area(self, height):
    """
        根据 self.radius 和 height 计算圆柱的面积
        :param height: 圆柱的高度，浮点数
        :return: 圆柱的面积，浮点数
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
    base_area = math.pi * self.radius ** 2
    lateral_area = 2 * math.pi * self.radius * height
    return 2 * base_area + lateral_area