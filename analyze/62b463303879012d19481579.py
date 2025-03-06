def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    
    Args:
        issue (str): El contenido del elemento 'issue' del que se extraerán los valores.
    
    Returns:
        tuple: Una tupla con dos elementos (number, suppl), donde 'number' es el número de la edición
               y 'suppl' es el suplemento si existe, o None si no se encuentra.
    """
    number = None
    suppl = None
    
    # Buscar el número en el texto
    import re
    number_match = re.search(r'\d+', issue)
    if number_match:
        number = int(number_match.group())
    
    # Buscar el suplemento en el texto
    suppl_match = re.search(r'suppl\.?\s*(\d+)', issue, re.IGNORECASE)
    if suppl_match:
        suppl = int(suppl_match.group(1))
    
    return number, suppl