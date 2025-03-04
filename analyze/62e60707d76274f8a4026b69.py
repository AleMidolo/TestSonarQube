def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    class Meta:
        abstract = False

    attrs = {
        '__module__': 'django.contrib.gis.db.models',
        'Meta': Meta,
        'objects': models.GeoManager(),
    }

    # Add the fields to the class
    for field_name, field_type in fields.items():
        attrs[field_name] = field_type

    # Add the SRID mapping if provided
    if srid_map:
        attrs['srid_map'] = srid_map

    # Create the new Point subclass
    return type(name, (models.Point,), attrs)