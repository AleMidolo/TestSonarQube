def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    # Initialize empty dictionary for observer schema
    observer_schema = {}
    
    # Process each key-value pair in manifest_dict
    for key, value in manifest_dict.items():
        
        # Handle nested dictionaries recursively
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
            
        # Handle nested lists recursively    
        elif isinstance(value, list):
            from generate_default_observer_schema_list import generate_default_observer_schema_list
            observer_schema[key] = generate_default_observer_schema_list(value)
            
        # For first level, preserve identifying fields
        elif first_level and key in ['apiVersion', 'kind', 'metadata']:
            observer_schema[key] = value
            
        # Set all other values to None    
        else:
            observer_schema[key] = None
            
    return observer_schema