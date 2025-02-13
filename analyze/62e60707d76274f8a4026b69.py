def point_type(name, fields, srid_map):
    from collections import namedtuple

    # Create a named tuple for the fields
    PointFields = namedtuple(name, fields)

    class Point(PointFields):
        def __init__(self, *args):
            super().__init__(*args)
            self.srid = srid_map.get(name, None)

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join(map(str, self))})"

    return Point