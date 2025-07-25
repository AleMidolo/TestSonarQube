def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    result = {}
    
    # Handle identity fields for first level resources
    if first_level:
        identity_fields = ['apiVersion', 'kind', 'metadata']
        for field in identity_fields:
            if field in manifest_dict:
                result[field] = manifest_dict[field]
    
    # Process all keys in manifest_dict
    for key, value in manifest_dict.items():
        # Skip identity fields if already processed
        if first_level and key in ['apiVersion', 'kind', 'metadata']:
            continue
            
        # Handle nested dictionaries recursively    
        if isinstance(value, dict):
            result[key] = generate_default_observer_schema_dict(value)
            
        # Handle lists recursively through generate_default_observer_schema_list
        elif isinstance(value, list):
            result[key] = generate_default_observer_schema_list(value)
            
        # Set all other values to None
        else:
            result[key] = None
            
    return result

def generate_default_observer_schema_list(manifest_list):
    """Helper function to handle lists in the manifest"""
    if not manifest_list:
        return []
        
    # Take first item as template
    first_item = manifest_list[0]
    
    if isinstance(first_item, dict):
        return [generate_default_observer_schema_dict(first_item)]
    elif isinstance(first_item, list):
        return [generate_default_observer_schema_list(first_item)]
    else:
        return [None]