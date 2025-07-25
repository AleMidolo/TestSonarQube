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
    
    if parts:
        # Assume the first part is the number
        number = parts[0]
        
        # Check if there is a supplement part
        if len(parts) > 1:
            suppl = parts[1]
    
    return number, suppl