import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    plugin_spec = {}
    
    # Assuming there is a 'spec.json' file in the plugin directory
    spec_file_path = os.path.join(plugin_dir, 'spec.json')
    
    if os.path.exists(spec_file_path):
        with open(spec_file_path, 'r') as spec_file:
            plugin_spec = json.load(spec_file)
    
    # Flatten the dictionary
    flat_spec = {}
    
    def flatten_dict(d, parent_key=''):
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                flatten_dict(v, new_key)
            else:
                flat_spec[new_key] = v

    flatten_dict(plugin_spec)
    
    return flat_spec