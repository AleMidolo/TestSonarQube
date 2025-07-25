def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    # Create new dictionary to store schema
    schema_dict = {}
    
    # Iterate through key-value pairs in manifest
    for key, value in manifest_dict.items():
        
        # Handle nested dictionaries recursively
        if isinstance(value, dict):
            schema_dict[key] = generate_default_observer_schema_dict(value)
            
        # Handle nested lists recursively    
        elif isinstance(value, list):
            from .utils import generate_default_observer_schema_list
            schema_dict[key] = generate_default_observer_schema_list(value)
            
        # For first level manifest, copy identifying fields
        elif first_level and key in ['apiVersion', 'kind', 'metadata']:
            schema_dict[key] = value
            
        # Set all other values to None
        else:
            schema_dict[key] = None
            
    return schema_dict