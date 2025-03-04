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
    suppl_indicators = ['suppl', 'supplement', 'sup']
    
    issue_lower = issue.lower()
    
    # Check if issue contains supplement
    for indicator in suppl_indicators:
        if indicator in issue_lower:
            # Extract supplement number if present
            parts = issue_lower.split(indicator)
            if len(parts) > 1:
                # Try to extract supplement number
                suppl_num = ''.join(filter(str.isdigit, parts[1]))
                suppl = suppl_num if suppl_num else '1'
            else:
                suppl = '1'
            
            # Extract main issue number if present
            number = ''.join(filter(str.isdigit, parts[0]))
            return number if number else None, suppl
    
    # If no supplement found, extract just the number
    number = ''.join(filter(str.isdigit, issue))
    return number if number else None, None