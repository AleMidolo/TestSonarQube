def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    
    Args:
        issue (str): El contenido del elemento 'issue'.
    
    Returns:
        tuple: Una tupla con dos elementos (number, suppl), donde:
            - number (str): El número extraído.
            - suppl (str): El suplemento extraído, si existe. Si no, será una cadena vacía.
    """
    number = ''
    suppl = ''
    
    if issue:
        # Buscar el suplemento (suppl) en el texto
        suppl_index = issue.lower().find('suppl')
        if suppl_index != -1:
            # Extraer el suplemento
            suppl = issue[suppl_index:].strip()
            # Extraer el número antes del suplemento
            number = issue[:suppl_index].strip()
        else:
            # Si no hay suplemento, el número es todo el contenido
            number = issue.strip()
    
    return number, suppl