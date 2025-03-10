def _replace_register(flow_params, register_number, register_value):
    """
    Reemplazar el valor de los flujos al número de registro dado

    La clave 'register_value' en el diccionario será reemplazada por el número de registro proporcionado por 'register_number'

    :param flow_params: Diccionario que contiene los flujos definidos  
    :param register_number: El número del registro donde se almacenará el valor  
    :param register_value: Clave que será reemplazada por el número de registro  
    """
    if isinstance(flow_params, dict):
        for key, value in flow_params.items():
            if key == register_value:
                flow_params[key] = register_number
            elif isinstance(value, dict):
                _replace_register(value, register_number, register_value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        _replace_register(item, register_number, register_value)
    return flow_params