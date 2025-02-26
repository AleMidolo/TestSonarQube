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
            observer_schema[key] = generate_default_observer_schema_dict(value, first_level)
        elif isinstance(value, list):
            observer_schema[key] = [generate_default_observer_schema_dict(item, first_level) if isinstance(item, dict) else None for item in value]
        else:
            if first_level and key in ['kind', 'apiVersion', 'metadata']:
                observer_schema[key] = value
            else:
                observer_schema[key] = None

    return observer_schema