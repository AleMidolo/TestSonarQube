import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    flattened_dict = {}
    
    # Check if the directory exists
    if not os.path.isdir(plugin_dir):
        raise FileNotFoundError(f"The directory {plugin_dir} does not exist.")
    
    # Look for a plugin specification file (e.g., plugin.json)
    plugin_spec_file = os.path.join(plugin_dir, "plugin.json")
    
    if not os.path.isfile(plugin_spec_file):
        raise FileNotFoundError(f"No plugin specification file found in {plugin_dir}.")
    
    # Load the plugin specification
    with open(plugin_spec_file, 'r') as file:
        plugin_spec = json.load(file)
    
    # Flatten the dictionary
    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flattened_dict = flatten_dict(plugin_spec)
    
    return flattened_dict