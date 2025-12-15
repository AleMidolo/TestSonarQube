class AreaCalculator: 
    def __init__(self, radius):
        """
        Initialize the radius for shapes.
        :param radius: float
        """
        self.radius = radius

    def calculate_circle_area(self):
        """
        calculate the area of circle based on self.radius
        :return: area of circle, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_circle_area()
        12.566370614359172
        """
        return math.pi * self.radius ** 2
    
    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sphere_area()
        50.26548245743669
        """
        return 4 * math.pi * self.radius ** 2
    
    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
        return 2 * math.pi * self.radius * (self.radius + height)
    
    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_sector_area(math.pi)
        6.283185307179586
        """
        return self.radius ** 2 * angle / 2
    
    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        计算环形区域的面积，基于内半径和外半径
        :param inner_radius: 扇形的内半径，浮点数
        :param outer_radius: 扇形的外半径，浮点数
        :return: 环形区域的面积，浮点数
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)