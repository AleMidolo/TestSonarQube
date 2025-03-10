def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    
    Args:
        issue (str): El contenido del elemento 'issue' que puede contener un número y/o un suplemento.
    
    Returns:
        tuple: Una tupla con dos elementos (number, suppl), donde:
            - number (str or None): El número extraído o None si no se encuentra.
            - suppl (str or None): El suplemento extraído o None si no se encuentra.
    """
    number = None
    suppl = None
    
    # Buscar el número (puede ser un número entero o decimal)
    import re
    number_match = re.search(r'\d+(\.\d+)?', issue)
    if number_match:
        number = number_match.group()
    
    # Buscar el suplemento (puede ser 's', 'suppl', 'supplement', etc.)
    suppl_match = re.search(r'(s|suppl|supplement)\s*(\d*)', issue, re.IGNORECASE)
    if suppl_match:
        suppl = suppl_match.group(2) if suppl_match.group(2) else '1'  # Si no hay número, asumir '1'
    
    return number, suppl