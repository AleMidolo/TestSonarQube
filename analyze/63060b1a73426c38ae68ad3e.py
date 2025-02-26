import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    flatten_dict = {}

    # Assuming there is a 'spec.json' file in the plugin directory
    spec_file_path = os.path.join(plugin_dir, 'spec.json')
    
    if os.path.exists(spec_file_path):
        with open(spec_file_path, 'r') as spec_file:
            spec_data = json.load(spec_file)
            flatten_dict = flatten(spec_data)
    
    return flatten_dict

def flatten(d, parent_key='', sep='_'):
    """
    Helper function to flatten a nested dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)