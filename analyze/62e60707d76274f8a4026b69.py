def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।
    """
    class Meta:
        pass
    
    attrs = {
        '__module__': 'gisfields.point',
        'Meta': Meta,
        'fields': fields,
        'srid_map': srid_map
    }
    
    return type(name, (object,), attrs)