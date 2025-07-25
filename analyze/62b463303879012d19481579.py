def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    """
    number = None
    suppl = None
    
    if issue is not None:
        issue_str = str(issue).strip()
        if issue_str:
            # Buscar el número principal
            number_match = re.search(r'\d+', issue_str)
            if number_match:
                number = int(number_match.group())
            
            # Buscar el suplemento (suppl)
            suppl_match = re.search(r'suppl\s*(\d+)', issue_str, re.IGNORECASE)
            if suppl_match:
                suppl = int(suppl_match.group(1))
            else:
                # Si no se encuentra 'suppl', verificar si hay un 's' seguido de un número
                suppl_match = re.search(r's\s*(\d+)', issue_str, re.IGNORECASE)
                if suppl_match:
                    suppl = int(suppl_match.group(1))
    
    return number, suppl