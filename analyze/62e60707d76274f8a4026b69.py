def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from collections import namedtuple

    # Crear una subclase de namedtuple con los campos dados
    PointSubclass = namedtuple(name, fields)

    # Agregar el atributo SRID basado en el mapa SRID proporcionado
    def __init__(self, *args, **kwargs):
        super(PointSubclass, self).__init__(*args, **kwargs)
        self.srid = srid_map.get(name, None)

    # Asignar el nuevo __init__ a la subclase
    PointSubclass.__init__ = __init__

    return PointSubclass