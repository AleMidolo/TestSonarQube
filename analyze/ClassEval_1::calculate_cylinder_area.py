def calculate_cylinder_area(self, height):
    """
        根据 self.radius 和 height 计算圆柱的面积
        :param height: 圆柱的高度，浮点数
        :return: 圆柱的面积，浮点数
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
    circle_area = 2 * math.pi * self.radius ** 2
    side_area = 2 * math.pi * self.radius * height
    return circle_area + side_area