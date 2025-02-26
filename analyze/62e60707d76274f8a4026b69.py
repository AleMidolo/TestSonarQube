def point_type(name, fields, srid_map):
    """
    动态创建一个 Point 子类。
    """
    from collections import namedtuple

    # Create a namedtuple for the Point
    Point = namedtuple(name, fields)

    # Add SRID mapping
    Point.srid_map = srid_map

    return Point