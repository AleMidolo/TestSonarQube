def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: Lista de comandos o cadena con saltos de línea.
    :param separator: Separador entre comandos (por defecto " && ").
    :return: Cadena con los comandos unidos en una sola línea.
    """
    if isinstance(script, str):
        commands = script.strip().split('\n')
    elif isinstance(script, list):
        commands = script
    else:
        raise ValueError("El script debe ser una cadena o una lista de comandos.")
    
    # Eliminar espacios en blanco y líneas vacías
    commands = [cmd.strip() for cmd in commands if cmd.strip()]
    
    # Unir comandos con el separador
    return separator.join(commands)