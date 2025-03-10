def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa che rappresenta il numero e il supplemento dell'issue.

    Returns:
        tuple: Una tupla contenente il numero (int) e il supplemento (str) estratti.
               Se il supplemento non è presente, il secondo elemento della tupla sarà None.
    """
    # Rimuovi eventuali spazi bianchi all'inizio e alla fine
    issue = issue.strip()
    
    # Cerca un numero all'inizio della stringa
    number_part = ''
    i = 0
    while i < len(issue) and issue[i].isdigit():
        number_part += issue[i]
        i += 1
    
    # Se non è stato trovato un numero, restituisci None per entrambi i valori
    if not number_part:
        return (None, None)
    
    # Converti il numero in intero
    number = int(number_part)
    
    # Il resto della stringa è il supplemento
    suppliment = issue[i:].strip() or None
    
    return (number, suppliment)