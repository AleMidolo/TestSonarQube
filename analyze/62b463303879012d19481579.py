def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    """
    number = None
    suppl = None
    
    # Assuming 'issue' is a string that may contain 'number' and 'suppl'
    if isinstance(issue, str):
        parts = issue.split()
        for part in parts:
            if part.startswith('number:'):
                number = part.split(':')[1]
            elif part.startswith('suppl:'):
                suppl = part.split(':')[1]
    
    return number, suppl