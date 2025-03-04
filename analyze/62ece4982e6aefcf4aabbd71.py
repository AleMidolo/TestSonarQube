def regex_dict(item):
    import re
    
    # Create new dict to store converted keys
    converted = {}
    
    # Iterate through original dict
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        regex_key = key.replace('.', '\\.').replace('*', '.*')
        # Add ^ and $ to match full string
        regex_key = f'^{regex_key}$'
        # Compile regex pattern and use as new key
        converted[re.compile(regex_key)] = value
        
    return converted