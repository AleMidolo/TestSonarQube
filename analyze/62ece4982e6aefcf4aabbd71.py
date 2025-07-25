def regex_dict(item):
    import re
    
    # Create new dictionary to store converted keys
    converted = {}
    
    # Iterate through original dictionary
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        # Escape dots, replace * with .* 
        regex_key = key.replace('.', '\\.').replace('*', '.*')
        
        # Add regex pattern as key with original value
        converted[regex_key] = value
        
    return converted