import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    flatten_dict = {}
    
    # Check if the directory exists
    if not os.path.exists(plugin_dir):
        return flatten_dict
    
    # Look for a plugin spec file (e.g., plugin.json)
    spec_file = os.path.join(plugin_dir, "plugin.json")
    
    if not os.path.isfile(spec_file):
        return flatten_dict
    
    # Load the plugin spec file
    with open(spec_file, 'r') as file:
        plugin_spec = json.load(file)
    
    # Flatten the dictionary
    def flatten(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flatten_dict = flatten(plugin_spec)
    
    return flatten_dict