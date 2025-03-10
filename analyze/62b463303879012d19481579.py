def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa contenente il numero e il supplemento.

    Returns:
        tuple: Una tupla contenente il numero (int) e il supplemento (str).
    """
    # Rimuovi spazi bianchi e separa il numero dal supplemento
    issue = issue.strip()
    number_part = ''
    supplment_part = ''
    
    # Itera attraverso i caratteri per separare numero e supplemento
    for char in issue:
        if char.isdigit():
            number_part += char
        else:
            supplment_part += char
    
    # Converti il numero in intero, se presente
    number = int(number_part) if number_part else None
    
    return number, supplment_part.strip()