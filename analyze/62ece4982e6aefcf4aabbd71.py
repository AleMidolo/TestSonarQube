def regex_dict(item):
    import re
    
    # Create new dict to store transformed keys
    transformed = {}
    
    # Iterate through key-value pairs in input dict
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        # Escape dots, replace * with .* 
        regex_key = key.replace('.', '\.').replace('*', '.*')
        
        # Add to transformed dict with regex key and original value
        transformed[regex_key] = value
        
    return transformed