def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    Generates a new dictionary based on the `manifest_dict` where all non-dict and non-list values are replaced with `None`.
    If `first_level` is True, the function copies the identifying fields from the manifest.

    Args:
        manifest_dict (dict): Partial Kubernetes resources.
        first_level (bool, optional): If True, indicates that the dictionary represents the entire `observer_schema` of a Kubernetes resource.

    Returns:
        dict: The generated partial `observer_schema`.
    """
    observer_schema = {}
    
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value)
        else:
            if first_level and key in ['apiVersion', 'kind', 'metadata']:
                observer_schema[key] = value
            else:
                observer_schema[key] = None
    
    return observer_schema

def generate_default_observer_schema_list(manifest_list):
    """
    Generates a new list based on the `manifest_list` where all non-dict and non-list values are replaced with `None`.

    Args:
        manifest_list (list): Partial Kubernetes resources in list format.

    Returns:
        list: The generated partial `observer_schema`.
    """
    observer_schema = []
    
    for item in manifest_list:
        if isinstance(item, dict):
            observer_schema.append(generate_default_observer_schema_dict(item))
        elif isinstance(item, list):
            observer_schema.append(generate_default_observer_schema_list(item))
        else:
            observer_schema.append(None)
    
    return observer_schema