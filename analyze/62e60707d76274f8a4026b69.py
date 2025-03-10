def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.

    :param name: Nome della sottoclasse da creare.
    :param fields: Lista di campi (attributi) da aggiungere alla sottoclasse.
    :param srid_map: Dizionario che mappa i nomi dei campi ai rispettivi SRID.
    :return: La sottoclasse creata.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in fields:
                setattr(self, field, kwargs.get(field, None))
            self.srid_map = srid_map

        def __repr__(self):
            fields_repr = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({fields_repr}, srid_map={self.srid_map})"

    DynamicPoint.__name__ = name
    return DynamicPoint