def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Crea un diccionario plano a partir de la especificación del plugin.

    :param plugin_dir: Una ruta al directorio del plugin  
    :return: Un diccionario plano que contiene las propiedades del plugin
    """
    flattened = {}
    
    def flatten_dict(d, parent_key=''):
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten_dict(value, new_key)
            else:
                flattened[new_key] = value
                
    try:
        # Intenta leer el archivo spec.json del directorio del plugin
        import json
        import os
        
        spec_path = os.path.join(plugin_dir, 'spec.json')
        
        if not os.path.exists(spec_path):
            return {}
            
        with open(spec_path, 'r') as f:
            spec = json.load(f)
            
        # Aplana el diccionario recursivamente
        flatten_dict(spec)
        
        return flattened
        
    except Exception as e:
        print(f"Error al procesar la especificación del plugin: {str(e)}")
        return {}