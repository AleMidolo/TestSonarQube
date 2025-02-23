def point_type(name, fields, srid_map):
    """
    डायनामिक रूप से एक पॉइंट सबक्लास बनाएं।
    """
    # Create a new class dynamically
    class Point:
        def __init__(self, **kwargs):
            for field in fields:
                setattr(self, field, kwargs.get(field, None))
        
        def __repr__(self):
            return f"{name}(" + ", ".join(f"{field}={getattr(self, field)}" for field in fields) + ")"
    
    # Add SRID mapping
    Point.srid_map = srid_map
    
    return Point