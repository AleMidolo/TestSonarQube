def is_fill_compute_el(obj):
    # Check if object has both 'fill' and 'compute' attributes
    has_fill = hasattr(obj, 'fill')
    has_compute = hasattr(obj, 'compute')
    
    # If either attribute is missing, return False
    if not (has_fill and has_compute):
        return False
        
    # Get the attributes
    fill_attr = getattr(obj, 'fill')
    compute_attr = getattr(obj, 'compute')
    
    # Check if both attributes are callable (i.e. methods)
    return callable(fill_attr) and callable(compute_attr)