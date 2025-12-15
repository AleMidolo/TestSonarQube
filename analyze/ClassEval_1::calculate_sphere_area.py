def calculate_sphere_area(self):
        """
        根据 self.radius 计算球的面积
        :return: 球的面积，浮点数
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
        return 4 * math.pi * self.radius ** 2