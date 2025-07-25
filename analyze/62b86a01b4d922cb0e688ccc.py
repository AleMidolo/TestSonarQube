def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    # Initialize empty dictionary for observer schema
    observer_schema = {}
    
    # Iterate through key-value pairs in manifest dictionary
    for key, value in manifest_dict.items():
        
        # Handle nested dictionaries recursively
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
            
        # Handle lists by calling generate_default_observer_schema_list
        elif isinstance(value, list):
            from .utils import generate_default_observer_schema_list
            observer_schema[key] = generate_default_observer_schema_list(value)
            
        # For first level, copy identifying fields
        elif first_level and key in ['apiVersion', 'kind', 'metadata']:
            observer_schema[key] = value
            
        # For all other values, set to None
        else:
            observer_schema[key] = None
            
    return observer_schema