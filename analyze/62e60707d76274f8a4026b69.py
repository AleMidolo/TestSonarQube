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
        if isinstance(field_type, tuple):
            field_class, field_args = field_type
            attrs[field_name] = field_class(*field_args)
        else:
            attrs[field_name] = field_type()
            
    # Add geometry field with SRID mapping
    attrs['geom'] = models.PointField(srid=srid_map.get(name, 4326))
    
    # Create and return new Point subclass
    return type(name, (models.Model,), attrs)