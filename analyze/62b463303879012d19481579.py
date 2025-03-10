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
    
    # Split the issue string by spaces to separate potential number and supplement
    parts = issue.split()
    
    for part in parts:
        # Check if the part is a number
        if part.isdigit():
            number = int(part)
        # Check if the part is a supplement (e.g., 'Suppl', 'S', 'Supplement')
        elif part.lower() in ['suppl', 's', 'supplement']:
            suppl = part
    
    return number, suppl