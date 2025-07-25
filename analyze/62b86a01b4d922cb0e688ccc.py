def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    result = {}
    
    # Handle first level special fields that should be copied from manifest
    if first_level:
        identity_fields = ['apiVersion', 'kind', 'metadata']
        for field in identity_fields:
            if field in manifest_dict:
                result[field] = manifest_dict[field]
    
    # Process all fields in manifest_dict
    for key, value in manifest_dict.items():
        # Skip if key already processed for first level
        if first_level and key in result:
            continue
            
        # Handle nested dictionaries recursively
        if isinstance(value, dict):
            result[key] = generate_default_observer_schema_dict(value)
            
        # Handle lists recursively
        elif isinstance(value, list):
            # Import the list handling function
            from .utils import generate_default_observer_schema_list
            result[key] = generate_default_observer_schema_list(value)
            
        # For all other types, set value to None
        else:
            result[key] = None
            
    return result