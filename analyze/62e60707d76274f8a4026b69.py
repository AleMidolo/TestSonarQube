def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.

    :param name: Nome della sottoclasse da creare.
    :param fields: Lista di tuple (nome_campo, tipo_campo) per i campi aggiuntivi.
    :param srid_map: Dizionario che mappa i nomi dei campi agli SRID.
    :return: La sottoclasse creata.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        __slots__ = [field[0] for field in fields]

        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            for field, value in kwargs.items():
                setattr(self, field, value)

        @property
        def srid(self):
            for field, srid in srid_map.items():
                if hasattr(self, field):
                    return srid
            return None

    DynamicPoint.__name__ = name
    return DynamicPoint