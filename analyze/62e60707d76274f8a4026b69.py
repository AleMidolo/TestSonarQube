def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from collections import namedtuple

    # Crear una subclase de namedtuple con los campos dados
    PointSubclass = namedtuple(name, fields)

    # Agregar el atributo srid_map a la subclase
    PointSubclass.srid_map = srid_map

    return PointSubclass