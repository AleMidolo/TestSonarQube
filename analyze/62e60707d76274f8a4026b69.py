def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in fields:
                setattr(self, field, kwargs.get(field))
            self.srid = srid_map.get(name, 4326)  # Default SRID is 4326 (WGS84)

        def __repr__(self):
            fields_str = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_str}, srid={self.srid})"

    DynamicPoint.__name__ = name
    return DynamicPoint