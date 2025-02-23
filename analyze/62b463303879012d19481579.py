def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    """
    number = None
    suppl = None
    
    # Assuming 'issue' is a string that may contain 'number' and 'suppl'
    import re
    
    number_match = re.search(r'number\s*:\s*(\d+)', issue, re.IGNORECASE)
    suppl_match = re.search(r'suppl\s*:\s*(\w+)', issue, re.IGNORECASE)
    
    if number_match:
        number = number_match.group(1)
    
    if suppl_match:
        suppl = suppl_match.group(1)
    
    return number, suppl