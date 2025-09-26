import math


class AreaCalculator:

    def __init__(self, radius):
        self._radius = radius  # Encapsulated field

    @property
    def radius(self):
        return self._radius

    def calculate_circle_area(self):
        return self._calculate_circle_area()

    def calculate_sphere_area(self):
        return self._calculate_sphere_area()

    def calculate_cylinder_area(self, height):
        return self._calculate_cylinder_area(height)

    def calculate_sector_area(self, angle):
        return self._calculate_sector_area(angle)

    def calculate_annulus_area(self, inner_radius, outer_radius):
        return self._calculate_annulus_area(inner_radius, outer_radius)

    def _calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def _calculate_sphere_area(self):
        return 4 * math.pi * self.radius ** 2

    def _calculate_cylinder_area(self, height):
        return 2 * math.pi * self.radius * (self.radius + height)

    def _calculate_sector_area(self, angle):
        return self.radius ** 2 * angle / 2

    def _calculate_annulus_area(self, inner_radius, outer_radius):
        return math.pi * (outer_radius ** 2 - inner_radius ** 2)