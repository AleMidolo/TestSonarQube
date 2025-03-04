def remove_ending_os_sep(input_list):
    import os
    
    # Handle None input
    if input_list is None:
        return []
        
    # Check input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
        
    result = []
    
    # Process each string in list
    for path in input_list:
        # Skip if not string
        if not isinstance(path, str):
            result.append(path)
            continue
            
        # Skip if empty or single char
        if len(path) <= 1:
            result.append(path)
            continue
            
        # Remove trailing separator if exists
        if path[-1] == os.sep:
            result.append(path[:-1])
        else:
            result.append(path)
            
    return result