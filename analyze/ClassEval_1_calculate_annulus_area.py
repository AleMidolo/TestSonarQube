import math

def calculate_annulus_area(self, inner_radius, outer_radius):
    """
    inner_radius और outer_radius के आधार पर एनलस का एरिया कैलकुलेट करें।

    :param inner_radius: सेक्टर का इनर रेडियस, float
    :param outer_radius: सेक्टर का आउटर रेडियस, float
    :return: एनलस का एरिया, float

    >>> areaCalculator.calculate_annulus_area(2, 3)
    15.707963267948966
    """
    # Annulus area = π * (outer_radius² - inner_radius²)
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)