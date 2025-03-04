def regex_dict(item):
    import re
    
    # Create new dict to store transformed keys
    transformed = {}
    
    # Iterate through key-value pairs in input dict
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        # Escape dots, replace * with .* 
        regex_key = key.replace('.', '\\.').replace('*', '.*')
        
        # Add regex key and original value to new dict
        transformed[regex_key] = value
        
    return transformed