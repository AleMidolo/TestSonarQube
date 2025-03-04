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
    }
    
    # Add the fields to the class attributes
    for field in fields:
        attrs[field] = None
        
    # Add the SRID mapping
    attrs['srid_map'] = srid_map
    
    # Create the new class dynamically
    return type(name, (object,), attrs)