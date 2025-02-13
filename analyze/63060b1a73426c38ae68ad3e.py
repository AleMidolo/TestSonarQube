import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    def flatten_dict(d, parent_key='', sep='.'):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    spec_file_path = os.path.join(plugin_dir, 'plugin_spec.json')
    if not os.path.isfile(spec_file_path):
        raise FileNotFoundError(f"Spec file not found: {spec_file_path}")

    with open(spec_file_path, 'r') as f:
        spec = json.load(f)

    return flatten_dict(spec)