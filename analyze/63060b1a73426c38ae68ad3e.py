import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    flat_dict = {}
    
    # Assumiamo che il file di specifiche sia chiamato 'spec.json'
    spec_file = os.path.join(plugin_dir, 'spec.json')
    
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"File {spec_file} non trovato nella directory del plugin.")
    
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
    
    flat_dict = flatten_dict(spec_data)
    
    return flat_dict