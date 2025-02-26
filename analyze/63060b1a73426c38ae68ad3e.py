def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un diccionario plano a partir de la especificación del plugin.

    :param plugin_dir: Una ruta al directorio del plugin  
    :return: Un diccionario plano que contiene las propiedades del plugin
    """
    import os
    import json

    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    plugin_spec_path = os.path.join(plugin_dir, 'plugin_spec.json')
    
    if not os.path.exists(plugin_spec_path):
        raise FileNotFoundError(f"No plugin specification found at {plugin_spec_path}")

    with open(plugin_spec_path, 'r') as f:
        plugin_spec = json.load(f)

    return flatten_dict(plugin_spec)