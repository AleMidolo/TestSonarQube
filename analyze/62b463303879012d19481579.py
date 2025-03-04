def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.
    """
    number = None
    supplement = None
    
    if 'number' in issue:
        number = issue['number']
    
    if 'supplement' in issue:
        supplement = issue['supplement']
    
    return number, supplement