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
            
            # Get number before supplement
            if parts[0].strip():
                number = parts[0].strip()
                
            # Get supplement number if exists
            if len(parts) > 1 and parts[1].strip():
                suppl = parts[1].strip()
                # Remove any leading/trailing punctuation
                suppl = suppl.strip('.:() ')
            else:
                suppl = '1' # Default supplement number
                
            return number, suppl
    
    # If no supplement found, assume it's just an issue number
    try:
        number = issue.strip('.:() ')
        return number, None
    except:
        return None, None