def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in fields:
                setattr(self, field, None)
                
        def __str__(self):
            field_str = ', '.join(f'{field}={getattr(self, field)}' for field in fields)
            return f"{name}({field_str}, srid={self.srid})"
            
        @property
        def srid(self):
            return srid_map.get(self.__class__.__name__, 4326)
            
    DynamicPoint.__name__ = name
    return DynamicPoint