import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un diccionario plano a partir de la especificación del plugin.

    :param plugin_dir: Una ruta al directorio del plugin  
    :return: Un diccionario plano que contiene las propiedades del plugin
    """
    spec_file = os.path.join(plugin_dir, 'plugin_spec.json')
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"El archivo de especificación del plugin no se encontró en {plugin_dir}")
    
    with open(spec_file, 'r') as file:
        spec_data = json.load(file)
    
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