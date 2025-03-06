def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    :param issue: L'elemento issue da cui estrarre numero e supplemento.
    :return: Una tupla contenente il numero e il supplemento (se presenti).
    """
    number = None
    supplement = None
    
    if issue is not None:
        # Supponiamo che l'elemento issue sia una stringa con formato "numero-supplemento"
        parts = issue.split('-')
        if len(parts) > 0:
            number = parts[0]
        if len(parts) > 1:
            supplement = parts[1]
    
    return number, supplement