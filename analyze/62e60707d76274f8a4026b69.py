def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।
    """
    class Meta:
        pass
    
    attrs = {
        '__module__': 'django.contrib.gis.db.models',
        '_meta': Meta(),
        'objects': None,
        'srid_map': srid_map,
    }
    
    # Add the fields to the attributes
    for field_name, field in fields.items():
        attrs[field_name] = field
        
    # Create the new Point subclass
    return type(name, (Point,), attrs)