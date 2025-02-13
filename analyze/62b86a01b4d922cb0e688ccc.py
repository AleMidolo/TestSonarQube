def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    new_dict = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            new_dict[key] = generate_default_observer_schema_dict(value, False)
        elif isinstance(value, list):
            new_dict[key] = [generate_default_observer_schema_dict(item, False) if isinstance(item, dict) else None for item in value]
        else:
            if first_level and key in ['apiVersion', 'kind', 'metadata']:
                new_dict[key] = value
            else:
                new_dict[key] = None
    return new_dict