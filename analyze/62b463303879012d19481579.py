def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa contenente il numero e il supplemento.

    Returns:
        tuple: Una tupla contenente il numero (int) e il supplemento (str, se presente, altrimenti None).
    """
    # Rimuovi eventuali spazi bianchi all'inizio e alla fine
    issue = issue.strip()
    
    # Cerca un numero seguito da un supplemento (es. "123A")
    if issue[-1].isalpha():
        number = int(issue[:-1])
        supplement = issue[-1]
    else:
        number = int(issue)
        supplement = None
    
    return number, supplement