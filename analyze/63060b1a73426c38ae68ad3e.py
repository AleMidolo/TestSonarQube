def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    import os
    import json

    def flatten_dict(d, parent_key='', sep='.'):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    plugin_spec_path = os.path.join(plugin_dir, 'plugin_spec.json')
    
    if not os.path.exists(plugin_spec_path):
        raise FileNotFoundError(f"Plugin spec file not found at {plugin_spec_path}")

    with open(plugin_spec_path, 'r') as f:
        plugin_spec = json.load(f)

    return flatten_dict(plugin_spec)