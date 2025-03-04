def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.
    """
    number = None
    supplement = None
    
    if issue:
        # Remove any whitespace
        issue = issue.strip()
        
        # Check if there's a supplement indicator (usually after a space)
        if ' ' in issue:
            parts = issue.split(' ', 1)
            number = parts[0]
            supplement = parts[1]
        else:
            number = issue
            
    return number, supplement