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
    
    # Iterate over all files in the plugin directory
    for root, dirs, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Flatten the dictionary
                    for key, value in data.items():
                        if isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                flat_dict[f"{key}.{sub_key}"] = sub_value
                        else:
                            flat_dict[key] = value
    return flat_dict