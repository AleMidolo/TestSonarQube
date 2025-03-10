def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa contenente il numero e il supplemento.

    Returns:
        tuple: Una tupla contenente il numero e il supplemento (se presente).
    """
    # Rimuovi eventuali spazi bianchi all'inizio e alla fine
    issue = issue.strip()
    
    # Cerca un numero seguito da un supplemento (es. "123A")
    if len(issue) > 1 and issue[-1].isalpha():
        number = issue[:-1]
        supplement = issue[-1]
        return number, supplement
    else:
        # Se non c'è un supplemento, restituisci solo il numero
        return issue, None