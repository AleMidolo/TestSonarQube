def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    Together with :func:``generate_default_observer_schema_list``, this function is
    called recursively to generate part of a default ``observer_schema`` from part of a
    Kubernetes resource, defined respectively by ``manifest_dict`` or ``manifest_list``.

    Args:
        manifest_dict (dict): Partial Kubernetes resources
        first_level (bool, optional): If True, indicates that the dictionary represents
            the whole observer schema of a Kubernetes resource

    Returns:
        dict: Generated partial observer_schema

    This function creates a new dictionary from ``manifest_dict`` and replaces all
    non-list and non-dict values by ``None``.

    In case of ``first_level`` dictionary (i.e. complete ``observer_schema`` for a
    resource), the values of the identifying fields are copied from the manifest file.
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
    Together with :func:``generate_default_observer_schema_dict``, this function is
    called recursively to generate part of a default ``observer_schema`` from part of a
    Kubernetes resource, defined respectively by ``manifest_dict`` or ``manifest_list``.

    Args:
        manifest_list (list): Partial Kubernetes resources

    Returns:
        list: Generated partial observer_schema

    This function creates a new list from ``manifest_list`` and replaces all
    non-list and non-dict values by ``None``.
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