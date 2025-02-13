def dehydrate_point(value):
    if not isinstance(value, Point):
        raise ValueError("Expected a Point instance")
    
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z if hasattr(value, 'z') else None
    }