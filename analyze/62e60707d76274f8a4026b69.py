def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = fields
            self.srid = srid_map.get(self.srid, None)

        def __repr__(self):
            return f"{name}({super().__repr__()}, fields={self.fields}, srid={self.srid})"

    DynamicPoint.__name__ = name
    return DynamicPoint