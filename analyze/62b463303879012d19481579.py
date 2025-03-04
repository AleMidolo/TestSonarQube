def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    number = None
    suppl = None
    
    if issue is None:
        return number, suppl
        
    # Convert issue to string and strip whitespace
    issue_text = str(issue).strip()
    
    if not issue_text:
        return number, suppl
        
    # Check for supplement indicator
    if 'suppl' in issue_text.lower():
        parts = issue_text.lower().split('suppl')
        
        # Extract number before suppl if it exists
        if parts[0].strip():
            try:
                number = int(parts[0].strip())
            except ValueError:
                number = None
                
        # Extract supplement number if it exists
        if len(parts) > 1 and parts[1].strip():
            try:
                suppl = int(parts[1].strip())
            except ValueError:
                try:
                    # Try parsing first character if full parse fails
                    suppl = int(parts[1].strip()[0])
                except (ValueError, IndexError):
                    suppl = None
    else:
        # Just try to parse as number if no supplement
        try:
            number = int(issue_text)
        except ValueError:
            number = None
            
    return number, suppl