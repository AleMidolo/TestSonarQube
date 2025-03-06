import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    spec_file = os.path.join(plugin_dir, 'plugin_spec.json')
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"Plugin spec file not found in {plugin_dir}")

    with open(spec_file, 'r') as f:
        spec_data = json.load(f)

    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return flatten_dict(spec_data)