def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    
    Args:
        issue (str): The issue string to extract number and suppl from.
    
    Returns:
        tuple: A tuple containing the extracted number and suppl values.
              If no number or suppl is found, returns (None, None).
    """
    number = None
    suppl = None
    
    # Example logic to extract number and suppl
    # This is a placeholder and should be replaced with actual logic
    if issue:
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = int(part)
            elif part.lower().startswith('suppl'):
                suppl = part
    
    return number, suppl