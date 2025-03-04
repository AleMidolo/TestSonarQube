def _replace_register(flow_params, register_number, register_value):
    """
    Reemplazar el valor de los flujos al número de registro dado

    La clave 'register_value' en el diccionario será reemplazada por el número de registro proporcionado por 'register_number'

    :param flow_params: Diccionario que contiene los flujos definidos  
    :param register_number: El número del registro donde se almacenará el valor  
    :param register_value: Clave que será reemplazada por el número de registro  
    """
    # Recorrer el diccionario de manera recursiva
    for key, value in flow_params.items():
        # Si el valor es un diccionario, llamar recursivamente
        if isinstance(value, dict):
            _replace_register(value, register_number, register_value)
        # Si el valor es una lista, revisar cada elemento
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    _replace_register(item, register_number, register_value)
        # Si el valor coincide con register_value, reemplazarlo
        elif value == register_value:
            flow_params[key] = register_number