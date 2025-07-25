def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa contenente il numero e il supplemento.

    Returns:
        tuple: Una tupla contenente il numero (int) e il supplemento (str).
    """
    # Rimuovi eventuali spazi bianchi
    issue = issue.strip()
    
    # Trova il numero e il supplemento
    number = ''
    suppl = ''
    for char in issue:
        if char.isdigit():
            number += char
        else:
            suppl += char
    
    # Converti il numero in intero
    number = int(number) if number else 0
    
    return number, suppl