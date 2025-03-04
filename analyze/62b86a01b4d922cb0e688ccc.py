def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    observer_schema = {}
    
    # Process each key-value pair in the manifest dictionary
    for key, value in manifest_dict.items():
        
        # Handle first level identifiers
        if first_level and key in ['apiVersion', 'kind', 'metadata']:
            observer_schema[key] = value
            continue
            
        # Recursively process nested dictionaries
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
            
        # Recursively process lists    
        elif isinstance(value, list):
            from generate_default_observer_schema_list import generate_default_observer_schema_list
            observer_schema[key] = generate_default_observer_schema_list(value)
            
        # Set all other values to None    
        else:
            observer_schema[key] = None
            
    return observer_schema