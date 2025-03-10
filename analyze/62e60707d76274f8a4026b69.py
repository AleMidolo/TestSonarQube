def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.

    :param name: Nome della sottoclasse.
    :param fields: Dizionario che mappa i nomi dei campi ai loro tipi.
    :param srid_map: Dizionario che mappa i nomi dei campi ai loro SRID.
    :return: La sottoclasse creata.
    """
    from shapely.geometry import Point

    class DynamicPoint(Point):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._fields = fields
            self._srid_map = srid_map

        def __getattr__(self, name):
            if name in self._fields:
                return self._fields[name]
            elif name in self._srid_map:
                return self._srid_map[name]
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

        def __setattr__(self, name, value):
            if name in self._fields:
                self._fields[name] = value
            elif name in self._srid_map:
                self._srid_map[name] = value
            else:
                super().__setattr__(name, value)

    DynamicPoint.__name__ = name
    return DynamicPoint