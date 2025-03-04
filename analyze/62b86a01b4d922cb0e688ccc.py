def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    result = {}
    
    # Handle identifying fields at first level
    identifying_fields = ['apiVersion', 'kind', 'metadata']
    
    for key, value in manifest_dict.items():
        if first_level and key in identifying_fields:
            # Copy identifying fields as-is at first level
            result[key] = value
        elif isinstance(value, dict):
            # Recursively process nested dictionaries
            result[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            # Process lists using helper function
            from .utils import generate_default_observer_schema_list
            result[key] = generate_default_observer_schema_list(value)
        else:
            # Replace all other values with None
            result[key] = None
            
    return result