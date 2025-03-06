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
    
    # Example logic to extract number and supplement
    # This is a placeholder and should be replaced with actual logic based on the issue format
    if issue:
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = int(part)
            elif part.lower().startswith('suppl'):
                suppl = part
    
    return number, suppl