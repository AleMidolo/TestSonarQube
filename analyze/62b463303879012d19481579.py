def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    """
    number = None
    suppl = None
    
    if issue:
        # Split the issue string by '-' to separate number and supplement
        parts = issue.split('-')
        if len(parts) > 0:
            # The first part is assumed to be the number
            number = parts[0].strip()
            if len(parts) > 1:
                # The second part is assumed to be the supplement
                suppl = parts[1].strip()
    
    return number, suppl