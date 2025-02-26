def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    from collections import namedtuple
    from shapely.geometry import Point

    # Create a named tuple for the fields
    PointFields = namedtuple(name, fields)

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = PointFields(*args)

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join(map(str, self.fields))})"

        @property
        def srid(self):
            return srid_map.get(self.__class__.__name__, None)

    return DynamicPoint