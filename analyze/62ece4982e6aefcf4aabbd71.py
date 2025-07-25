def regex_dict(item):
    import re
    
    # Create new dictionary to store converted keys
    converted = {}
    
    # Iterate through original dictionary
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        # Escape dots, replace * with .* 
        regex_key = key.replace('.', '\\.').replace('*', '.*')
        # Add ^ and $ to match full string
        regex_key = f'^{regex_key}$'
        
        # Add converted key and original value to new dict
        converted[regex_key] = value
        
    return converted