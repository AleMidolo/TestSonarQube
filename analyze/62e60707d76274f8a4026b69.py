def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    from collections import namedtuple

    # Create a namedtuple with the given fields
    Point = namedtuple(name, fields)

    # Add the SRID map as a class attribute
    Point.srid_map = srid_map

    return Point