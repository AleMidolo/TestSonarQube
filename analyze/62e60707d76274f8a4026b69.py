from shapely.geometry import Point

def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.
    """
    attrs = {field: None for field in fields}

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in fields:
                setattr(self, field, kwargs.get(field, None))

        def __repr__(self):
            return f"{name}({', '.join(f'{field}={getattr(self, field)}' for field in fields)})"

    DynamicPoint.__name__ = name
    DynamicPoint.srid_map = srid_map
    return DynamicPoint