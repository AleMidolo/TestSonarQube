def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from collections import namedtuple

    # Crear una clase base Point
    class Point:
        def __init__(self, x, y, srid=None):
            self.x = x
            self.y = y
            self.srid = srid

        def __repr__(self):
            return f"Point(x={self.x}, y={self.y}, srid={self.srid})"

    # Crear una subclase dinámica de Point
    DynamicPoint = type(name, (Point,), {})

    # Agregar campos adicionales a la subclase
    for field_name, field_type in fields.items():
        setattr(DynamicPoint, field_name, field_type)

    # Agregar el mapeo SRID
    DynamicPoint.srid_map = srid_map

    return DynamicPoint