def remove_ending_os_sep(input_list):
    import os

    # Handle None input
    if input_list is None:
        return []

    # Check input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")

    result = []
    for path in input_list:
        # Check if path is string
        if not isinstance(path, str):
            raise TypeError("List elements must be strings")
            
        # Check if path length > 1 and ends with separator
        if len(path) > 1 and path.endswith(os.sep):
            result.append(path[:-1])
        else:
            result.append(path)
            
    return result