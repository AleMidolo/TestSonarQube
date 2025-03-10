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
    if issue and issue[-1].isalpha():
        number = issue[:-1]
        supplement = issue[-1]
        try:
            number = int(number)
            return number, supplement
        except ValueError:
            pass
    
    # Se non c'è un supplemento, prova a convertire l'intera stringa in un numero
    try:
        number = int(issue)
        return number, None
    except ValueError:
        pass
    
    # Se non è possibile estrarre un numero, restituisci None per entrambi i valori
    return None, None