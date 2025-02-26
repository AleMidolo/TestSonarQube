def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    number = None
    suppl = None
    
    # Assuming issue is a string that may contain number and suppl information
    if isinstance(issue, str):
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = part
            elif part.lower().startswith('suppl'):
                suppl = part
    
    return number, suppl