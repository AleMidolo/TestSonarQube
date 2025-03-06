import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    flat_dict = {}
    
    # Check if the directory exists
    if not os.path.exists(plugin_dir):
        raise FileNotFoundError(f"The directory {plugin_dir} does not exist.")
    
    # Look for a spec file (e.g., plugin_spec.json) in the plugin directory
    spec_file = os.path.join(plugin_dir, "plugin_spec.json")
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"No plugin specification file found in {plugin_dir}.")
    
    # Load the spec file
    with open(spec_file, 'r') as f:
        spec_data = json.load(f)
    
    # Flatten the dictionary
    def flatten_dict(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flat_dict = flatten_dict(spec_data)
    
    return flat_dict