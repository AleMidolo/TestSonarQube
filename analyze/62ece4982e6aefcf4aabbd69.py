def _replace_register(flow_params, register_number, register_value):
    """
    Reemplazar el valor de los flujos al número de registro dado

    La clave 'register_value' en el diccionario será reemplazada por el número de registro proporcionado por 'register_number'

    :param flow_params: Diccionario que contiene los flujos definidos  
    :param register_number: El número del registro donde se almacenará el valor  
    :param register_value: Clave que será reemplazada por el número de registro  
    """
    if 'register_value' in flow_params:
        flow_params['register_value'] = register_number
    return flow_params