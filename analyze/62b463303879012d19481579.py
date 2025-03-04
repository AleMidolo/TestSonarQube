def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extrae los posibles valores de 'number' y 'suppl' a partir del contenido de 'issue'.
    """
    if not issue:
        return None, None
        
    # Remove any whitespace
    issue = issue.strip()
    
    # Check for supplement indicator
    suppl = None
    number = None
    
    # Common supplement indicators
    suppl_indicators = ['Suppl', 'suppl', 'Supplement', 'supplement', 'S']
    
    for indicator in suppl_indicators:
        if indicator in issue:
            # Split on supplement indicator
            parts = issue.split(indicator)
            
            # Get number part
            if parts[0].strip():
                number = parts[0].strip()
            
            # Get supplement part if it exists
            if len(parts) > 1 and parts[1].strip():
                suppl = parts[1].strip()
                # Remove any leading/trailing punctuation
                suppl = suppl.strip('.:() ')
            else:
                suppl = '1' # Default supplement number
                
            return number, suppl
    
    # If no supplement found, treat entire string as issue number
    # Remove any punctuation/spaces
    number = issue.strip('.:() ')
    
    return number, suppl