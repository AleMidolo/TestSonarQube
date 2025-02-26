def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = fields
            self.srid = srid_map.get(name, None)

        def __repr__(self):
            return f"{name}({self.x}, {self.y}, srid={self.srid})"

    DynamicPoint.__name__ = name
    return DynamicPoint