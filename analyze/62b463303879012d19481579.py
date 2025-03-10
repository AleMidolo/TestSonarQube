def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    
    Args:
        issue (str): The issue string from which to extract the number and supplement.
    
    Returns:
        tuple: A tuple containing the extracted number and supplement (number, suppl).
               If no number or supplement is found, returns (None, None).
    """
    number = None
    suppl = None
    
    # Split the issue string into parts based on common delimiters
    parts = issue.replace('-', ' ').replace('_', ' ').split()
    
    for part in parts:
        # Check if the part is a number
        if part.isdigit():
            number = int(part)
        # Check if the part is a supplement (e.g., 'Suppl', 'S', 's')
        elif part.lower() in ['suppl', 's']:
            suppl = part
    
    return number, suppl