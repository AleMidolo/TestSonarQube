def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.
    """
    # Aquí se asume que hay un diccionario que contiene las especificaciones de las opciones
    option_specs = {
        'command1': {
            'arg1': {'type': 'string', 'required': True},
            'arg2': {'type': 'int', 'required': False}
        },
        'command2': {
            'arg1': {'type': 'bool', 'required': False},
            'arg2': {'type': 'float', 'required': True}
        }
    }
    
    # Verificar si el comando existe
    if command_name in option_specs:
        # Verificar si el argumento existe
        if argument_name in option_specs[command_name]:
            return option_specs[command_name][argument_name]
    
    # Si no se encuentra la especificación, devolver None o lanzar una excepción
    return None