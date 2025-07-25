def oneline(script, separator=" && "):
    """
    Convierte un script en un comando de una sola linea.  
    Esto es util para ejecutar un único comando SSH y pasar un script en una sola linea.

    :param script: String con el script a convertir
    :param separator: Separador entre comandos, por defecto " && "
    :return: String con el script en una sola línea
    """
    # Dividir el script en líneas y eliminar líneas vacías
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    
    # Unir las líneas usando el separador
    return separator.join(lines)