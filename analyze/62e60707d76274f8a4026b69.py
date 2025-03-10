def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from collections import namedtuple
    return namedtuple(name, fields + ['srid'])._make([None] * (len(fields) + 1))._replace(srid=srid_map)