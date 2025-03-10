def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    
    Args:
        issue (str): El contenido del elemento 'issue'.
    
    Returns:
        tuple: Una tupla con dos elementos (number, suppl), donde 'number' es el número de la edición
               y 'suppl' es el suplemento, si existe. Si no se encuentra un número o suplemento, se devuelve None.
    """
    number = None
    suppl = None
    
    # Buscar el número en el formato "Número X"
    if "Número" in issue:
        parts = issue.split("Número")
        number_part = parts[1].strip()
        number = ''.join(filter(str.isdigit, number_part))
    
    # Buscar el suplemento en el formato "Suplemento X"
    if "Suplemento" in issue:
        parts = issue.split("Suplemento")
        suppl_part = parts[1].strip()
        suppl = ''.join(filter(str.isdigit, suppl_part))
    
    # Si no se encuentra en el formato anterior, intentar extraer el número y suplemento directamente
    if number is None and suppl is None:
        # Asumir que el número y suplemento están separados por un guion o espacio
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                if number is None:
                    number = part
                else:
                    suppl = part
    
    return (number, suppl)