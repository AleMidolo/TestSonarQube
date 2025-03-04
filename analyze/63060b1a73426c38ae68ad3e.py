def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un dizionario non annidato a partire dalle specifiche del plugin.

    :param plugin_dir: Un percorso alla directory del plugin  
    :return: Un dizionario piatto che contiene le proprietà del plugin
    """
    flattened = {}
    
    def flatten_dict(d, parent_key=''):
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten_dict(value, new_key)
            else:
                flattened[new_key] = value
                
    # Leggi il file delle specifiche
    spec_file = os.path.join(plugin_dir, 'plugin.json')
    if not os.path.exists(spec_file):
        spec_file = os.path.join(plugin_dir, 'plugin.yaml')
        
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"No plugin specification file found in {plugin_dir}")
        
    # Carica le specifiche
    with open(spec_file, 'r') as f:
        if spec_file.endswith('.json'):
            import json
            specs = json.load(f)
        else:
            import yaml
            specs = yaml.safe_load(f)
            
    # Appiattisci il dizionario
    flatten_dict(specs)
    
    return flattened