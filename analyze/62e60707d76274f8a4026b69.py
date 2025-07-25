def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.
    """
    from shapely.geometry import Point
    from shapely.geometry.base import BaseGeometry

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = fields
            self.srid = srid_map.get(name, None)

        def __repr__(self):
            return f"{name}({', '.join(map(str, self.coords))})"

    DynamicPoint.__name__ = name
    return DynamicPoint