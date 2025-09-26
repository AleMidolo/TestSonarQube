import math


class AreaCalculator:

    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return self._circle_area(self.radius)

    def calculate_sphere_area(self):
        return self._sphere_area(self.radius)

    def calculate_cylinder_area(self, height):
        return self._cylinder_area(self.radius, height)

    def calculate_sector_area(self, angle):
        return self._sector_area(self.radius, angle)

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return self._annulus_area(inner_radius, outer_radius)

    @staticmethod
    def _circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def _sphere_area(radius):
        return 4 * math.pi * radius ** 2

    @staticmethod
    def _cylinder_area(radius, height):
        return 2 * math.pi * radius * (radius + height)

    @staticmethod
    def _sector_area(radius, angle):
        return radius ** 2 * angle / 2

    @staticmethod
    def _annulus_area(inner_radius, outer_radius):
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)