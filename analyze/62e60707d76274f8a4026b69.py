def point_type(name, fields, srid_map):
    """
    Crear dinámicamente una subclase de 'Point'.
    """
    from django.contrib.gis.db import models
    
    class Meta:
        abstract = True

    attrs = {
        '__module__': 'django.contrib.gis.db.models',
        'Meta': Meta,
    }

    # Add fields to attrs dictionary
    for field_name, field_type in fields.items():
        attrs[field_name] = field_type

    # Add SRID mapping if provided
    if srid_map:
        attrs['srid_map'] = srid_map

    # Create and return new Point subclass
    return type(name, (models.Point,), attrs)