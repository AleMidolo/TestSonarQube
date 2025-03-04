def point_type(name, fields, srid_map):
    """
    Crea dinamicamente una sottoclasse di Point.
    """
    from shapely.geometry import Point
    
    # Create new class dictionary
    class_dict = {}
    
    # Add fields as class attributes
    for field in fields:
        class_dict[field] = None
        
    # Add srid mapping
    class_dict['srid_map'] = srid_map
    
    # Create new class dynamically
    new_class = type(name, (Point,), class_dict)
    
    return new_class