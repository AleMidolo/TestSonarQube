def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    
    Args:
        issue (str): The issue string to extract number and supplement from.
    
    Returns:
        tuple: A tuple containing the extracted number and supplement (number, suppl).
               If no number or supplement is found, returns (None, None).
    """
    number = None
    suppl = None
    
    # Split the issue string into parts based on common delimiters
    parts = issue.replace('-', ' ').replace('(', ' ').replace(')', ' ').split()
    
    for part in parts:
        if part.isdigit():
            number = int(part)
        elif part.lower().startswith('s'):
            suppl = part[1:] if part[1:].isdigit() else None
    
    return number, suppl