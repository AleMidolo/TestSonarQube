def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    Junto con la función :func:`generate_default_observer_schema_list`, esta función se llama de manera recursiva para generar parte de un ``observer_schema`` predeterminado a partir de una parte de un recurso de Kubernetes, definido respectivamente por ``manifest_dict`` o ``manifest_list``.

    Argumentos:
    **manifest_dict (dict):** Recursos parciales de Kubernetes.
    **first_level (bool, opcional):** Si es True, indica que el diccionario representa el esquema completo del observador (observer schema) de un recurso de Kubernetes.

    Retorna:
    **dict:** Esquema parcial generado (`observer_schema`).

    Esta función crea un nuevo diccionario a partir de ``manifest_dict`` y reemplaza todos los valores que no sean listas (`list`) ni diccionarios (`dict`) por ``None``.

    En el caso de un diccionario de ``first_level`` (es decir, un ``observer_schema`` completo para un recurso), los valores de los campos identificadores se copian del archivo de manifiesto.
    """
    observer_schema = {}
    
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value)
        else:
            if first_level and key in ['apiVersion', 'kind', 'metadata']:
                observer_schema[key] = value
            else:
                observer_schema[key] = None
    
    return observer_schema

def generate_default_observer_schema_list(manifest_list):
    """
    Junto con la función :func:`generate_default_observer_schema_dict`, esta función se llama de manera recursiva para generar parte de un ``observer_schema`` predeterminado a partir de una parte de un recurso de Kubernetes, definido respectivamente por ``manifest_dict`` o ``manifest_list``.

    Argumentos:
    **manifest_list (list):** Recursos parciales de Kubernetes.

    Retorna:
    **list:** Esquema parcial generado (`observer_schema`).

    Esta función crea una nueva lista a partir de ``manifest_list`` y reemplaza todos los valores que no sean listas (`list`) ni diccionarios (`dict`) por ``None``.
    """
    observer_schema = []
    
    for item in manifest_list:
        if isinstance(item, dict):
            observer_schema.append(generate_default_observer_schema_dict(item))
        elif isinstance(item, list):
            observer_schema.append(generate_default_observer_schema_list(item))
        else:
            observer_schema.append(None)
    
    return observer_schema