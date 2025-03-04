def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Construye el tipo de argumento complejo.

    :param subcommand: el nombre del comando
    :param type_name: el nombre del tipo complejo 
    :param option_name: el nombre de la opción
    :param spec_option: las especificaciones de la opción
    :return: la instancia del tipo complejo
    """
    # Mapeo de tipos complejos conocidos
    type_mapping = {
        'json': JsonType,
        'key-value': KeyValueType,
        'list': ListType,
        'dict': DictType
    }

    # Obtener la clase del tipo complejo
    type_class = type_mapping.get(type_name.lower())
    
    if not type_class:
        raise ValueError(f"Tipo complejo desconocido: {type_name}")

    try:
        # Crear instancia del tipo complejo con los parámetros
        type_instance = type_class(
            subcommand=subcommand,
            option_name=option_name,
            spec=spec_option
        )
        return type_instance
        
    except Exception as e:
        raise ValueError(f"Error al crear tipo complejo {type_name}: {str(e)}")