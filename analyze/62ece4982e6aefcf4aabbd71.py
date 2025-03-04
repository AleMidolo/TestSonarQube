def regex_dict(item):
    import re
    
    # Create new dict to store regex keys
    regex_keys = {}
    
    # Iterate through each key-value pair
    for key, value in item.items():
        # Convert wildcard pattern to regex pattern
        # Escape special regex chars
        regex_pattern = re.escape(key)
        # Replace \* with .* to match any chars
        regex_pattern = regex_pattern.replace('\\*', '.*')
        # Add start and end anchors
        regex_pattern = f'^{regex_pattern}$'
        
        # Add converted key and original value to new dict
        regex_keys[regex_pattern] = value
        
    return regex_keys