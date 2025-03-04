def _replace_register(flow_params, register_number, register_value):
    """
    Reemplazar el valor de los flujos al número de registro dado

    La clave 'register_value' en el diccionario será reemplazada por el número de registro proporcionado por 'register_number'

    :param flow_params: Diccionario que contiene los flujos definidos  
    :param register_number: El número del registro donde se almacenará el valor  
    :param register_value: Clave que será reemplazada por el número de registro  
    """
    # Si flow_params es un diccionario
    if isinstance(flow_params, dict):
        # Iterar sobre cada clave y valor
        for key, value in flow_params.items():
            # Si el valor es un diccionario, llamada recursiva
            if isinstance(value, dict):
                _replace_register(value, register_number, register_value)
            # Si el valor es una lista, procesar cada elemento
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        _replace_register(item, register_number, register_value)
            # Si el valor coincide con register_value, reemplazarlo
            elif value == register_value:
                flow_params[key] = register_number