def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    result = {}
    
    # Handle first level special fields
    if first_level:
        # Copy identifier fields from manifest
        identifier_fields = ['apiVersion', 'kind', 'metadata']
        for field in identifier_fields:
            if field in manifest_dict:
                result[field] = manifest_dict[field]
    
    # Process all fields in manifest_dict
    for key, value in manifest_dict.items():
        # Skip if key already processed for first level
        if first_level and key in result:
            continue
            
        if isinstance(value, dict):
            # Recursively process nested dictionaries
            result[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            # Process lists using a helper function
            result[key] = generate_default_observer_schema_list(value)
        else:
            # Set non-dict and non-list values to None
            result[key] = None
            
    return result

def generate_default_observer_schema_list(manifest_list):
    """Helper function to process lists in the manifest"""
    if not manifest_list:
        return []
        
    # Take first item as sample
    sample = manifest_list[0]
    
    if isinstance(sample, dict):
        return [generate_default_observer_schema_dict(sample)]
    elif isinstance(sample, list):
        return [generate_default_observer_schema_list(sample)]
    else:
        return [None]