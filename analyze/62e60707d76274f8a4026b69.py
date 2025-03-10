def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in fields:
                setattr(self, field, kwargs.get(field))
            self.srid = srid_map.get(name, None)

        def __repr__(self):
            return f"{name}({', '.join(f'{field}={getattr(self, field)}' for field in fields)})"

    DynamicPoint.__name__ = name
    return DynamicPoint