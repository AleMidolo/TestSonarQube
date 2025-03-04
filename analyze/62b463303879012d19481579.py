def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    if issue is None:
        return None, None
        
    # Remove any whitespace
    issue_text = issue.strip()
    
    if not issue_text:
        return None, None
        
    # Split on spaces to separate number and supplement
    parts = issue_text.split()
    
    number = None
    suppl = None
    
    # Extract number from first part
    if parts:
        try:
            number = int(parts[0])
        except ValueError:
            number = parts[0]
            
    # Check for supplement in remaining parts
    if len(parts) > 1:
        suppl = ' '.join(parts[1:])
        
    return number, suppl