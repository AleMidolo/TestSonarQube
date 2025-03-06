def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.

    :param name: Nome della sottoclasse da creare.
    :param fields: Lista di campi aggiuntivi da aggiungere alla sottoclasse.
    :param srid_map: Dizionario che mappa i nomi dei campi ai loro SRID.
    :return: La sottoclasse creata.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            for field in fields:
                setattr(self, field, kwargs.get(field))

        def __repr__(self):
            fields_repr = ', '.join(f"{field}={getattr(self, field)}" for field in fields)
            return f"{name}({super().__repr__()}, {fields_repr})"

        def to_wkt(self):
            wkt = super().wkt
            for field in fields:
                wkt += f", {field}={getattr(self, field)}"
            return wkt

        def get_srid(self, field):
            return srid_map.get(field, None)

    DynamicPoint.__name__ = name
    return DynamicPoint