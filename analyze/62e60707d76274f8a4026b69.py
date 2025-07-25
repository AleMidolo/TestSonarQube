def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = fields
            self.srid = srid_map.get(name, None)

        def get_fields(self):
            return self.fields

        def get_srid(self):
            return self.srid

    DynamicPoint.__name__ = name
    return DynamicPoint